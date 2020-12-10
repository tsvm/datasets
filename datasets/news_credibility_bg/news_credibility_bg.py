# coding=utf-8
# Copyright 2020 The HuggingFace Datasets Authors and the current dataset script contributor.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""TODO: Add a description here."""

from __future__ import absolute_import, division, print_function

import csv
import json
import os

import datasets

_CITATION = """\
@InProceedings{news_credibility_bg,
title = {In Search of Credible News},
author={Hardalov, Momchil and Koychev, Ivan and Nakov, Preslav},
year={2016},
publisher={Springer International Publishing},
url={https://link.springer.com/chapter/10.1007/978-3-319-44748-3_17}
}
"""

_DESCRIPTION = """\
We study the problem of finding fake online news. This is an important problem as news of questionable credibility have recently been proliferating in social media at an alarming scale. As this is an understudied problem, especially for languages other than English, we first collect and release to the research community three new balanced credible vs. fake news datasets derived from four online sources.
"""

_HOMEPAGE = ""

_LICENSE = ""

# TODO: Add link to the official dataset URLs here
# The HuggingFace dataset library don't host the datasets but only point to the original files
# This can be an arbitrary nested dict/list of URLs (see below in `_split_generators` method)
_URLs = {
    'news': "https://github.com/mhardalov/news-credibility/blob/master/datasets/news.tar.gz",
    'abstracts': "https://github.com/mhardalov/news-credibility/blob/master/datasets/word2vec.tar.gz"
}

# The file contains sources from several categories
NEWS_SOURCES = {
    "nenovinite": "ne!novinite-data-extended.json",
    "bazikileaks": "bazikileaks-data-extended.json", 
    "btv": "btv-lifestyle-data-extended.json"
}


# For one of the available datasets, the credibility can be recognized from the new category name.
NEWS_SOURCE_BOTH_CREDIBLE_FAKE = "btv-lifestyle-data-extended.json"
CREDIBLE_NEWS_CATEGORY = "Лайфстайл"


# TODO: Name of the dataset usually match the script name with CamelCase instead of snake_case
class NewDataset(datasets.GeneratorBasedBuilder):
    """TODO: Short description of my dataset."""

    VERSION = datasets.Version("1.1.0")

    # This is an example of a dataset with multiple configurations.
    # If you don't want/need to define several sub-sets in your dataset,
    # just remove the BUILDER_CONFIG_CLASS and the BUILDER_CONFIGS attributes.

    # If you need to make complex sub-parts in the datasets with configurable options
    # You can create your own builder configuration class to store attribute, inheriting from datasets.BuilderConfig
    # BUILDER_CONFIG_CLASS = MyBuilderConfig

    # You will be able to load one or the other configurations in the following list with
    # data = datasets.load_dataset('my_dataset', 'first_domain')
    # data = datasets.load_dataset('my_dataset', 'second_domain')
    BUILDER_CONFIGS = [
        datasets.BuilderConfig(name="news", version=VERSION, description="Fake or satirical news from several websites in Bulgarian."),
        datasets.BuilderConfig(name="abstracts", version=VERSION, description="Long abstracts from the Bulgarian DBPedia, used for training word vectors"),
    ]

    DEFAULT_CONFIG_NAME = "news"  # It's not mandatory to have a default configuration. Just use one if it make sense.

    def _info(self):
        # TODO: This method specifies the datasets.DatasetInfo object which contains informations and typings for the dataset
        if self.config.name == "news":  # This is the name of the configuration selected in BUILDER_CONFIGS above 
            features = datasets.Features(
                {   
                    "source": datasets.Value("string"),
                    "credible": datasets.Value("bool_"),
                    "key": datasets.Value("string"),
                    "url": datasets.Value("string"),
                    "html": datasets.Value("string"),
                    "title": datasets.Value("string"),
                    "content": datasets.Value("string"),
                    "category": datasets.Value("string"),
                    "publishDate": datasets.Value("string"),
                    "viewCount": datasets.Value("int8"),
                    "commentCount": datasets.Value("int8")
                }
            )
        elif self.config.name == "abstracts":  # This is an example to show how to have different features for "first_domain" and "second_domain"
            features = datasets.Features(
                {
                    "abstract": datasets.Value("string")
                }
            )
        return datasets.DatasetInfo(
            # This is the description that will appear on the datasets page.
            description=_DESCRIPTION,
            # This defines the different columns of the dataset and their types
            features=features,  # Here we define them above because they are different between the two configurations
            # If there's a common (input, target) tuple from the features,
            # specify them here. They'll be used if as_supervised=True in
            # builder.as_dataset.
            supervised_keys=None,
            # Homepage of the dataset for documentation
            homepage=_HOMEPAGE,
            # License for the dataset if available
            license=_LICENSE,
            # Citation for the dataset
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        # TODO: This method is tasked with downloading/extracting the data and defining the splits depending on the configuration
        # If several configurations are possible (listed in BUILDER_CONFIGS), the configuration selected by the user is in self.config.name

        # dl_manager is a datasets.download.DownloadManager that can be used to download and extract URLs
        # It can accept any type or nested list/dict and will give back the same structure with the url replaced with path to local files.
        # By default the archives will be extracted and a path to a cached folder where they are extracted is returned instead of the archive 
        my_urls = _URLs[self.config.name]
        data_dir = dl_manager.download_and_extract(my_urls)

        print("----------------------", data_dir)
        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "filepath": os.path.join(data_dir, "ne!novinite-data-extended.json"),
                    "split": "train",
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "filepath": os.path.join(data_dir, "bazikileaks-data-extended.json"),
                    "split": "train",
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "filepath": os.path.join(data_dir, "btv-lifestyle-data-extended.json"),
                    "split": "test"
                },
            ),
        ]

    def _generate_examples(self, filepath, split):
        """ Yields examples. """
        with open(filepath, encoding="utf-8") as f:
            for id_, row in enumerate(f):
                data = json.loads(row)
                if self.config.name == "fake_news":
                    yield id_, {
                        "source": _news_source_from_filepath(filepath),
                        "credible": self._news_credibility(filepath, data["category"]),
                        "key": data["key"] or data["url"],
                        "url": data["url"],
                        "html": data["html"],
                        "title": data["title"],
                        "content": data["content"],
                        "category": data["category"],
                        "publishDate": data["publishedDate"],
                        "viewCount": data["viewCount"],
                        "commentCount": data["commentCount"] or 0
                    }
                elif self.config.name == "abstracts":
                    yield id_, {
                        "abstract": data["abstract"]
                    }

        def _news_source_from_filepath(filepath):
            """ Returns the news source name from the filepath
            """
            print(filepath)
            # os.filepath
            # filepath.substring(filepath.indexof())



        def _news_credibility(self, filepath, category):
            """ Checks whether the given news article is credible.
                Some of the sources are known to be noncredible.
                One of the sources contains both credible and noncredible news,
                which can be recognized by the news category.

                Returns boolean value.
            """
            return filepath.endswith(NEWS_SOURCE_BOTH_CREDIBLE_NONCREDIBLE) \
                    and category == CREDIBLE_NEWS_CATEGORY






