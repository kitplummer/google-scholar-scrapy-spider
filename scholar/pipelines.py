# -*- coding: utf-8 -*-
import re

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ScholarPipeline:
    def process_item(self, item, spider):
        i = item['publishedData']
        sections = i.split("- ")
        print(sections)
        org = sections[2].strip()
        authors = sections[0].strip()

        if "," not in sections[1]:
            match = re.match(r'.*([1-3][0-9]{3})', sections[1])
            if match is not None:
                year = match.group(1).replace(" ", "")
                source = ""
            else:
                source = sections[1].strip()
                year = 0

        else:
            source = sections[1].strip().split(',')[0].strip().split('\xa0')[0].strip()
            year = sections[1].strip().split(",")[1].replace(" ", "")

        item['author'] = authors
        item['source'] = source
        item['year'] = year
        item ['org'] = org
        return item
