# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from django.conf import settings


class Migration(SchemaMigration):

    def forwards(self, orm):
        db_engine = settings.DATABASES['default']['ENGINE']
        
        if db_engine.rfind('mysql') == -1:
            # Adding model 'Country'
            db.create_table('locations_country', (
                ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
                ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
                ('country_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2, db_index=True)),
                ('border', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(blank=True, null=True, geography=True)),
            ))
            db.send_create_signal('locations', ['Country'])

            # Adding model 'Region'
            db.create_table('locations_region', (
                ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
                ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
                ('code', self.gf('django.db.models.fields.CharField')(max_length=2, db_index=True)),
                ('border', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(blank=True, null=True, geography=True)),
                ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.Country'])),
            ))
            db.send_create_signal('locations', ['Region'])

            # Adding unique constraint on 'Region', fields ['country', 'code']
            db.create_unique('locations_region', ['country_id', 'code'])

            # Adding model 'City'
            db.create_table('locations_city', (
                ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
                ('name', self.gf('django.db.models.fields.CharField')(max_length=128, db_index=True)),
                ('coordinates', self.gf('locations.fields.CoordinateField')(blank=True, null=True, geography=True)),
                ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.Region'], null=True, blank=True)),
                ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.Country'])),
            ))
            db.send_create_signal('locations', ['City'])

            # Adding model 'Location'
            db.create_table('locations_location', (
                ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
                ('name', self.gf('django.db.models.fields.CharField')(max_length=128, db_index=True)),
                ('coordinates', self.gf('locations.fields.CoordinateField')(blank=True, null=True, geography=True)),
                ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.Country'])),
                ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.City'], null=True, blank=True)),
                ('description', self.gf('django.db.models.fields.TextField')(max_length=1024, null=True, blank=True)),
                ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photologue.Photo'], null=True, blank=True)),
                ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['category.Category'], null=True, blank=True)),
            ))
            db.send_create_signal('locations', ['Location'])
            
        # create MySQL tables without spatial indices so that it will work with InnoDB
        else:
            sql = """SET FOREIGN_KEY_CHECKS=0;
                    CREATE TABLE `locations_country` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(50) NOT NULL, `country_code` varchar(2) NOT NULL UNIQUE, `border` MULTIPOLYGON NULL);
                    CREATE TABLE `locations_region` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(128) NOT NULL, `code` varchar(2) NOT NULL, `border` MULTIPOLYGON NULL, `country_id` integer NOT NULL);
                    ALTER TABLE `locations_region` ADD CONSTRAINT `locations_region_country_id_545200d9bb67aa36_uniq` UNIQUE (`country_id`, `code`);
                    CREATE TABLE `locations_city` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(128) NOT NULL, `coordinates` POINT NULL, `region_id` integer NULL, `country_id` integer NOT NULL);
                    CREATE TABLE `locations_location` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(128) NOT NULL, `coordinates` POINT NULL, `country_id` integer NOT NULL, `city_id` integer NULL, `description` longtext NULL, `photo_id` integer NULL, `category_id` integer NULL);
                    CREATE INDEX `locations_region_65da3d2c` ON `locations_region` (`code`);
                    ALTER TABLE `locations_region` ADD CONSTRAINT `country_id_refs_id_688446d03ef69106` FOREIGN KEY (`country_id`) REFERENCES `locations_country` (`id`);
                    CREATE INDEX `locations_region_534dd89` ON `locations_region` (`country_id`);
                    CREATE INDEX `locations_city_52094d6e` ON `locations_city` (`name`);
                    ALTER TABLE `locations_city` ADD CONSTRAINT `region_id_refs_id_4877f50311a5997e` FOREIGN KEY (`region_id`) REFERENCES `locations_region` (`id`);
                    CREATE INDEX `locations_city_f6a8b032` ON `locations_city` (`region_id`);
                    ALTER TABLE `locations_city` ADD CONSTRAINT `country_id_refs_id_51bbc9cfa50a0b7d` FOREIGN KEY (`country_id`) REFERENCES `locations_country` (`id`);
                    CREATE INDEX `locations_city_534dd89` ON `locations_city` (`country_id`);
                    CREATE INDEX `locations_location_52094d6e` ON `locations_location` (`name`);
                    ALTER TABLE `locations_location` ADD CONSTRAINT `country_id_refs_id_3a0bfa099c9ea063` FOREIGN KEY (`country_id`) REFERENCES `locations_country` (`id`);
                    CREATE INDEX `locations_location_534dd89` ON `locations_location` (`country_id`);
                    ALTER TABLE `locations_location` ADD CONSTRAINT `city_id_refs_id_136a507ad0769b15` FOREIGN KEY (`city_id`) REFERENCES `locations_city` (`id`);
                    CREATE INDEX `locations_location_586a73b5` ON `locations_location` (`city_id`);
                    ALTER TABLE `locations_location` ADD CONSTRAINT `photo_id_refs_id_764ca670382ba838` FOREIGN KEY (`photo_id`) REFERENCES `photologue_photo` (`id`);
                    CREATE INDEX `locations_location_7c6c8bb1` ON `locations_location` (`photo_id`);
                    ALTER TABLE `locations_location` ADD CONSTRAINT `category_id_refs_id_71ba6eba4d7f8101` FOREIGN KEY (`category_id`) REFERENCES `category_category` (`id`);
                    CREATE INDEX `locations_location_42dc49bc` ON `locations_location` (`category_id`);"""

            db.execute(sql)

            db.send_create_signal('locations', ['Country'])
            db.send_create_signal('locations', ['Region'])
            db.send_create_signal('locations', ['City'])
            db.send_create_signal('locations', ['Location'])            

    def backwards(self, orm):
        # Removing unique constraint on 'Region', fields ['country', 'code']
        db.delete_unique('locations_region', ['country_id', 'code'])

        # Deleting model 'Country'
        db.delete_table('locations_country')

        # Deleting model 'Region'
        db.delete_table('locations_region')

        # Deleting model 'City'
        db.delete_table('locations_city')

        # Deleting model 'Location'
        db.delete_table('locations_location')

    models = {
        'category.category': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['category.Category']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'locations.city': {
            'Meta': {'ordering': "('name',)", 'object_name': 'City'},
            'coordinates': ('locations.fields.CoordinateField', [], {'blank': 'True', 'null': 'True', 'geography': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.Region']", 'null': 'True', 'blank': 'True'})
        },
        'locations.country': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Country'},
            'border': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'blank': 'True', 'null': 'True', 'geography': 'True'}),
            'country_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'locations.location': {
            'Meta': {'object_name': 'Location'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['category.Category']", 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.City']", 'null': 'True', 'blank': 'True'}),
            'coordinates': ('locations.fields.CoordinateField', [], {'blank': 'True', 'null': 'True', 'geography': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.Country']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photologue.Photo']", 'null': 'True', 'blank': 'True'})
        },
        'locations.region': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('country', 'code'),)", 'object_name': 'Region'},
            'border': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'blank': 'True', 'null': 'True', 'geography': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_index': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'photologue.photo': {
            'Meta': {'ordering': "['-date_added']", 'object_name': 'Photo'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '10', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'photo_related'", 'null': 'True', 'to': "orm['photologue.PhotoEffect']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tags': ('photologue.models.TagField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'title_slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'photologue.photoeffect': {
            'Meta': {'object_name': 'PhotoEffect'},
            'background_color': ('django.db.models.fields.CharField', [], {'default': "'#FFFFFF'", 'max_length': '7'}),
            'brightness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'color': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'contrast': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'filters': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'reflection_size': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'reflection_strength': ('django.db.models.fields.FloatField', [], {'default': '0.6'}),
            'sharpness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'transpose_method': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        }
    }

    complete_apps = ['locations']