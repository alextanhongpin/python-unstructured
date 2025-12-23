

``` python
from time import perf_counter as pc

from unstructured.partition.auto import partition
from unstructured.staging.base import elements_to_json

t0 = pc()


elements = partition(filename="./assets/files/resume-sample.pdf")
for element in elements:
    print(elements)
    print("\n")


print(elements_to_json(elements, filename="output.json"))


print(pc() - t0)
```

    IOPub data rate exceeded.
    The Jupyter server will temporarily stop sending output
    to the client in order to avoid crashing it.
    To change this limit, set the config variable
    `--ServerApp.iopub_data_rate_limit`.

    Current values:
    ServerApp.iopub_data_rate_limit=1000000.0 (bytes/sec)
    ServerApp.rate_limit_window=3.0 (secs)

    [
        {
            "element_id": "a2a2f5e11ab0fa191c638aae9a20285a",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            212.8,
                            163.0
                        ],
                        [
                            212.8,
                            183.1
                        ],
                        [
                            404.8,
                            183.1
                        ],
                        [
                            404.8,
                            163.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 1
            },
            "text": "RESUME SAMPLES",
            "type": "Title"
        },
        {
            "element_id": "cc23138894eb24a8caeba30d37b94807",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            209.8
                        ],
                        [
                            72.0,
                            223.8
                        ],
                        [
                            509.9,
                            223.8
                        ],
                        [
                            509.9,
                            209.8
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 1,
                "parent_id": "a2a2f5e11ab0fa191c638aae9a20285a"
            },
            "text": "Preparing an effective resume is a difficult and time-consuming task. This handout",
            "type": "NarrativeText"
        },
        {
            "element_id": "8c8fdcf2ebeda0f357c9434d45881f92",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            234.1
                        ],
                        [
                            72.0,
                            248.2
                        ],
                        [
                            524.9,
                            248.2
                        ],
                        [
                            524.9,
                            234.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 1,
                "parent_id": "a2a2f5e11ab0fa191c638aae9a20285a"
            },
            "text": "contains resume examples that will help you get started. Different formats and styles",
            "type": "NarrativeText"
        },
        {
            "element_id": "99baa9431110902f41be26a0902f57dd",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            258.5
                        ],
                        [
                            72.0,
                            272.6
                        ],
                        [
                            491.0,
                            272.6
                        ],
                        [
                            491.0,
                            258.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 1,
                "parent_id": "a2a2f5e11ab0fa191c638aae9a20285a"
            },
            "text": "are used to illustrate the various suggestions and tips contained in the handout,",
            "type": "NarrativeText"
        },
        {
            "element_id": "8761e1b55d06b00175d5bd098022aafd",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            282.9
                        ],
                        [
                            72.0,
                            296.9
                        ],
                        [
                            535.8,
                            296.9
                        ],
                        [
                            535.8,
                            282.9
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 1
            },
            "text": "\"Preparing Your Resume,\" also available through the Bellevue University Career Services",
            "type": "Title"
        },
        {
            "element_id": "321bc012183e81dfc8c8e0bf69891867",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            307.2
                        ],
                        [
                            72.0,
                            321.3
                        ],
                        [
                            113.6,
                            321.3
                        ],
                        [
                            113.6,
                            307.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 1
            },
            "text": "Center.",
            "type": "Title"
        },
        {
            "element_id": "b53f51509ac84d58aad43438dcad361b",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            349.6
                        ],
                        [
                            72.0,
                            363.6
                        ],
                        [
                            538.2,
                            363.6
                        ],
                        [
                            538.2,
                            349.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 1,
                "parent_id": "321bc012183e81dfc8c8e0bf69891867"
            },
            "text": "Remember, these are intended to serve only as examples. You should modify or change",
            "type": "NarrativeText"
        },
        {
            "element_id": "2ba4e55f9b75ebf3d0e6fa95d5136a7b",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            374.0
                        ],
                        [
                            72.0,
                            388.0
                        ],
                        [
                            537.4,
                            388.0
                        ],
                        [
                            537.4,
                            374.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 1,
                "parent_id": "321bc012183e81dfc8c8e0bf69891867"
            },
            "text": "as appropriate to customize your resume according to your skills, experience, education,",
            "type": "NarrativeText"
        },
        {
            "element_id": "cc60a692c10b926d496530653dd4b9f9",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            398.3
                        ],
                        [
                            72.0,
                            412.4
                        ],
                        [
                            228.6,
                            412.4
                        ],
                        [
                            228.6,
                            398.3
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 1,
                "parent_id": "321bc012183e81dfc8c8e0bf69891867"
            },
            "text": "and the job you\u2019re applying.",
            "type": "NarrativeText"
        },
        {
            "element_id": "c2e7fdff9b6d52c46ca0050ecb2d9759",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            447.1
                        ],
                        [
                            72.0,
                            461.1
                        ],
                        [
                            475.5,
                            461.1
                        ],
                        [
                            475.5,
                            447.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 1,
                "parent_id": "321bc012183e81dfc8c8e0bf69891867"
            },
            "text": "For additional guidance or assistance, contact the Career Services Center at",
            "type": "NarrativeText"
        },
        {
            "element_id": "1802068a990cfb976241c20529a866b8",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            471.4
                        ],
                        [
                            72.0,
                            485.5
                        ],
                        [
                            487.8,
                            485.5
                        ],
                        [
                            487.8,
                            471.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 1,
                "parent_id": "321bc012183e81dfc8c8e0bf69891867"
            },
            "text": "(402) 557-7423, (800) 756-7920 ext. 7423 or careerservices@bellevue.edu.",
            "type": "UncategorizedText"
        },
        {
            "element_id": "585dbc057a81c7199a5c271aa9b26037",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            551.8
                        ],
                        [
                            72.0,
                            679.0
                        ],
                        [
                            540.2,
                            679.0
                        ],
                        [
                            540.2,
                            551.8
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 1,
                "parent_id": "321bc012183e81dfc8c8e0bf69891867"
            },
            "text": "A Word of Caution: Please don\u2019t be tempted to use one of the Resume Wizards or Templates that are available online or included in many word processing programs. They can be difficult to work with, don\u2019t allow you to present yourself in the best possible light\u2014and employers can identify them easily. Instead, create your resume as a simple document in MS Word, like the examples included in this handout.",
            "type": "NarrativeText"
        },
        {
            "element_id": "edbfc5919daf54450ec5688840087bea",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            747.8
                        ],
                        [
                            72.0,
                            755.8
                        ],
                        [
                            139.3,
                            755.8
                        ],
                        [
                            139.3,
                            747.8
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 1
            },
            "text": "Revision: June 2015",
            "type": "Footer"
        },
        {
            "element_id": "8ee95aa06ba13e678ea9f5f597bd7285",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            331.2,
                            38.0
                        ],
                        [
                            331.2,
                            52.0
                        ],
                        [
                            543.6,
                            52.0
                        ],
                        [
                            543.6,
                            38.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 2
            },
            "text": "FUNCTIONAL (EXPERIENCED)",
            "type": "Header"
        },
        {
            "element_id": "294b023768b8d7145ceba24214e6520b",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            247.8,
                            71.0
                        ],
                        [
                            247.8,
                            134.3
                        ],
                        [
                            367.0,
                            134.3
                        ],
                        [
                            367.0,
                            71.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "links": [
                    {
                        "start_index": 76,
                        "text": "imasample1 @ xxx . com",
                        "url": "mailto:imasample1@xxx.com"
                    }
                ],
                "page_number": 2,
                "parent_id": "8ee95aa06ba13e678ea9f5f597bd7285"
            },
            "text": "IM A. SAMPLE I 1234 North 55 Street Bellevue, Nebraska 68005 (402) 292-2345 imasample1@xxx.com",
            "type": "UncategorizedText"
        },
        {
            "element_id": "3e76cdae78614400364fc7c617a2baae",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            209.7,
                            148.9
                        ],
                        [
                            209.7,
                            160.9
                        ],
                        [
                            405.4,
                            160.9
                        ],
                        [
                            405.4,
                            148.9
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 2,
                "parent_id": "8ee95aa06ba13e678ea9f5f597bd7285"
            },
            "text": "SUMMARY OF QUALIFICATIONS",
            "type": "Title"
        },
        {
            "element_id": "1fabce2589bb155378cf4ad96d153b3f",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            168.4
                        ],
                        [
                            72.0,
                            217.3
                        ],
                        [
                            534.1,
                            217.3
                        ],
                        [
                            534.1,
                            168.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 2,
                "parent_id": "3e76cdae78614400364fc7c617a2baae"
            },
            "text": "Exceptionally well organized and resourceful Professional with more than six years experience and a solid academic background in accounting and financial management; excellent analytical and problem solving skills; able to handle multiple projects while producing high quality work in a fast-paced, deadline-oriented environment.",
            "type": "NarrativeText"
        },
        {
            "element_id": "25e48b0d606fe0198c73ab92e028a645",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            269.3,
                            228.5
                        ],
                        [
                            269.3,
                            240.5
                        ],
                        [
                            345.7,
                            240.5
                        ],
                        [
                            345.7,
                            228.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 2,
                "parent_id": "8ee95aa06ba13e678ea9f5f597bd7285"
            },
            "text": "EDUCATION",
            "type": "Title"
        },
        {
            "element_id": "6f83fe05f9421bafc6e8aa2867395c14",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            247.9
                        ],
                        [
                            72.0,
                            259.0
                        ],
                        [
                            384.9,
                            259.0
                        ],
                        [
                            384.9,
                            247.9
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 2,
                "parent_id": "8ee95aa06ba13e678ea9f5f597bd7285"
            },
            "text": "Bachelor of Science, Bellevue University, Bellevue, NE (In Progress)",
            "type": "Title"
        },
        {
            "element_id": "786105a4b0c43cb4f50b5428352def4c",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            260.7
                        ],
                        [
                            108.0,
                            284.3
                        ],
                        [
                            297.8,
                            284.3
                        ],
                        [
                            297.8,
                            260.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 2,
                "parent_id": "8ee95aa06ba13e678ea9f5f597bd7285"
            },
            "text": "Major: Accounting Expected Graduation Date: January, 20xx",
            "type": "Title"
        },
        {
            "element_id": "6ead0c1b3eb955b8a88f49a42efd7215",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            360.1,
                            260.7
                        ],
                        [
                            360.1,
                            284.3
                        ],
                        [
                            537.7,
                            284.3
                        ],
                        [
                            537.7,
                            260.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 2,
                "parent_id": "8ee95aa06ba13e678ea9f5f597bd7285"
            },
            "text": "Minor: Computer Information Systems GPA to date: 3.95/4.00",
            "type": "Title"
        },
        {
            "element_id": "3bfe64393b662b65f2c1cd154117f909",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            195.1,
                            295.4
                        ],
                        [
                            195.1,
                            307.4
                        ],
                        [
                            419.9,
                            307.4
                        ],
                        [
                            419.9,
                            295.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 2,
                "parent_id": "8ee95aa06ba13e678ea9f5f597bd7285"
            },
            "text": "PROFESSIONAL ACCOMPLISHMENTS",
            "type": "Title"
        },
        {
            "element_id": "623a574e85fe84d579bfd6384f895912",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            315.2
                        ],
                        [
                            72.0,
                            365.6
                        ],
                        [
                            504.2,
                            365.6
                        ],
                        [
                            504.2,
                            315.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 2,
                "parent_id": "3bfe64393b662b65f2c1cd154117f909"
            },
            "text": "Accounting and Financial Management \uf0b7 Developed and maintained accounting records for up to fifty bank accounts. \uf0b7 Formulated monthly and year-end financial statements and generated various payroll records, including federal and state payroll reports, annual tax reports, W-2 and 1099 forms, etc.",
            "type": "NarrativeText"
        },
        {
            "element_id": "ea34b97723bf44c37821fb24541c2e0f",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            367.7
                        ],
                        [
                            72.0,
                            391.6
                        ],
                        [
                            538.1,
                            391.6
                        ],
                        [
                            538.1,
                            367.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 2,
                "parent_id": "3bfe64393b662b65f2c1cd154117f909"
            },
            "text": "Tested accuracy of account balances and prepared supporting documentation for submission during a comprehensive three-year audit of financial operations.",
            "type": "ListItem"
        },
        {
            "element_id": "8b7fd4a1059e7af482db7858444197ab",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            393.8
                        ],
                        [
                            72.0,
                            418.4
                        ],
                        [
                            382.8,
                            418.4
                        ],
                        [
                            382.8,
                            393.8
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 2,
                "parent_id": "3bfe64393b662b65f2c1cd154117f909"
            },
            "text": "Formulated intricate pro-forma budgets. \uf0b7 Calculated and implemented depreciation/amortization schedules.",
            "type": "ListItem"
        },
        {
            "element_id": "76ca4767f431c3a9746d1d1db7a29d4f",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            426.3
                        ],
                        [
                            72.0,
                            477.4
                        ],
                        [
                            521.0,
                            477.4
                        ],
                        [
                            521.0,
                            426.3
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 2,
                "parent_id": "3bfe64393b662b65f2c1cd154117f909"
            },
            "text": "Information Systems Analysis and Problem Solving \uf0b7 Converted manual to computerized accounting systems for two organizations. \uf0b7 Analyzed and successfully reprogrammed software to meet customer requirements. \uf0b7 Researched and corrected problems to assure effective operation of newly computerized systems.",
            "type": "NarrativeText"
        },
        {
            "element_id": "c4bff7363f9b81cd7aa25ab36e9cc33c",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            261.3,
                            488.5
                        ],
                        [
                            261.3,
                            499.5
                        ],
                        [
                            353.6,
                            499.5
                        ],
                        [
                            353.6,
                            488.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 2,
                "parent_id": "8ee95aa06ba13e678ea9f5f597bd7285"
            },
            "text": "WORK HISTORY",
            "type": "Title"
        },
        {
            "element_id": "32ff5e2fb0921f11843e663e1730ebea",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            506.9
                        ],
                        [
                            72.0,
                            530.6
                        ],
                        [
                            488.5,
                            530.6
                        ],
                        [
                            488.5,
                            506.9
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 2,
                "parent_id": "c4bff7363f9b81cd7aa25ab36e9cc33c"
            },
            "text": "Student Intern, Financial Accounting Development Program, Mutual of Omaha, Omaha, NE (Summer 20xx)",
            "type": "UncategorizedText"
        },
        {
            "element_id": "db2a001a33368c562c3b4c62c145351a",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            538.3
                        ],
                        [
                            72.0,
                            549.3
                        ],
                        [
                            432.9,
                            549.3
                        ],
                        [
                            432.9,
                            538.3
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 2,
                "parent_id": "8ee95aa06ba13e678ea9f5f597bd7285"
            },
            "text": "Accounting Coordinator, Nebraska Special Olympics, Omaha, NE (20xx-20xx)",
            "type": "Title"
        },
        {
            "element_id": "eea0409c8f0ffd9de8a0ff47e2b13772",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            556.9
                        ],
                        [
                            72.0,
                            567.9
                        ],
                        [
                            304.6,
                            567.9
                        ],
                        [
                            304.6,
                            556.9
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 2,
                "parent_id": "8ee95aa06ba13e678ea9f5f597bd7285"
            },
            "text": "Bookkeeper, SMC, Inc., Omaha, NE (20xx \u2013 20xx)",
            "type": "Title"
        },
        {
            "element_id": "4fc0ddbc42eed8285a09ec41b6269ea3",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            575.5
                        ],
                        [
                            72.0,
                            586.5
                        ],
                        [
                            387.8,
                            586.5
                        ],
                        [
                            387.8,
                            575.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 2,
                "parent_id": "8ee95aa06ba13e678ea9f5f597bd7285"
            },
            "text": "Bookkeeper, First United Methodist Church, Altus, OK (20xx \u2013 20xx)",
            "type": "Title"
        },
        {
            "element_id": "245418a690ff032b8db7a03753a7c16b",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            217.8,
                            601.1
                        ],
                        [
                            217.8,
                            613.1
                        ],
                        [
                            397.1,
                            613.1
                        ],
                        [
                            397.1,
                            601.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 2,
                "parent_id": "8ee95aa06ba13e678ea9f5f597bd7285"
            },
            "text": "PROFESSIONAL AFFILIATION",
            "type": "Title"
        },
        {
            "element_id": "7353f89d063588f90fe87ca747f1d22c",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            620.6
                        ],
                        [
                            72.0,
                            631.6
                        ],
                        [
                            309.8,
                            631.6
                        ],
                        [
                            309.8,
                            620.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 2,
                "parent_id": "8ee95aa06ba13e678ea9f5f597bd7285"
            },
            "text": "Member, IMA, Bellevue University Student Chapter",
            "type": "Title"
        },
        {
            "element_id": "0153c5fdc2cf0ffd07111c1fb2c62562",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            247.8,
                            646.3
                        ],
                        [
                            247.8,
                            658.3
                        ],
                        [
                            367.3,
                            658.3
                        ],
                        [
                            367.3,
                            646.3
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 2,
                "parent_id": "8ee95aa06ba13e678ea9f5f597bd7285"
            },
            "text": "COMPUTER SKILLS",
            "type": "Title"
        },
        {
            "element_id": "1373843c8a5a1db5ce67928afd52dcac",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            666.3
                        ],
                        [
                            72.0,
                            690.9
                        ],
                        [
                            421.5,
                            690.9
                        ],
                        [
                            421.5,
                            666.3
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 2,
                "parent_id": "0153c5fdc2cf0ffd07111c1fb2c62562"
            },
            "text": "Proficient in MS Office (Word, Excel, PowerPoint, Outlook), QuickBooks \uf0b7 Basic Knowledge of MS Access, SQL, Visual Basic, C++",
            "type": "ListItem"
        },
        {
            "element_id": "0c5423698bdbec17fb3537886a2a31f2",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            311.0,
                            52.4
                        ],
                        [
                            311.0,
                            66.4
                        ],
                        [
                            543.3,
                            66.4
                        ],
                        [
                            543.3,
                            52.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 3,
                "parent_id": "0153c5fdc2cf0ffd07111c1fb2c62562"
            },
            "text": "CHRONOLOGICAL (INTERNSHIP)",
            "type": "UncategorizedText"
        },
        {
            "element_id": "ca54a168e69e4b088824af156c2b03d7",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            85.3
                        ],
                        [
                            72.0,
                            98.2
                        ],
                        [
                            179.3,
                            98.2
                        ],
                        [
                            179.3,
                            85.3
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 3,
                "parent_id": "8ee95aa06ba13e678ea9f5f597bd7285"
            },
            "text": "IM A. SAMPLE II",
            "type": "Title"
        },
        {
            "element_id": "2c06f22ddbe8194787c8af3fdbefaa7d",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            413.1,
                            85.3
                        ],
                        [
                            413.1,
                            139.4
                        ],
                        [
                            543.1,
                            139.4
                        ],
                        [
                            543.1,
                            85.3
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 3,
                "parent_id": "8ee95aa06ba13e678ea9f5f597bd7285"
            },
            "text": "4321 South 55 Street Bellevue, Nebraska 68005 (402) 291-5432 imasample2@xxx.com",
            "type": "Title"
        },
        {
            "element_id": "175e5cbd02d08ce8ef753238cf479a9c",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            165.2
                        ],
                        [
                            72.0,
                            190.9
                        ],
                        [
                            525.2,
                            190.9
                        ],
                        [
                            525.2,
                            165.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 3,
                "parent_id": "2c06f22ddbe8194787c8af3fdbefaa7d"
            },
            "text": "OBJECTIVE: Internship or Part-time Position in Marketing, Public Relations or related field utilizing strong academic background and excellent communication skills",
            "type": "NarrativeText"
        },
        {
            "element_id": "3a43865175c27f64147deb7aa5bb440f",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            216.9
                        ],
                        [
                            72.0,
                            228.9
                        ],
                        [
                            152.4,
                            228.9
                        ],
                        [
                            152.4,
                            216.9
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 3,
                "parent_id": "2c06f22ddbe8194787c8af3fdbefaa7d"
            },
            "text": "EDUCATION:",
            "type": "UncategorizedText"
        },
        {
            "element_id": "2d2a6a48c50b7472d6050b867eb78db4",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            180.0,
                            216.9
                        ],
                        [
                            180.0,
                            242.5
                        ],
                        [
                            478.9,
                            242.5
                        ],
                        [
                            478.9,
                            216.9
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 3,
                "parent_id": "8ee95aa06ba13e678ea9f5f597bd7285"
            },
            "text": "BS in Business Administration with Marketing Emphasis Bellevue University, Bellevue, NE",
            "type": "Title"
        },
        {
            "element_id": "d2ca36998803ab4f1702bfe52cf2c582",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            198.0,
                            245.1
                        ],
                        [
                            198.0,
                            288.8
                        ],
                        [
                            420.7,
                            288.8
                        ],
                        [
                            420.7,
                            245.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 3,
                "parent_id": "2d2a6a48c50b7472d6050b867eb78db4"
            },
            "text": "Expected Graduation Date: June, 20xx \uf0b7 GPA to date: 3.56/4.00 Relevant Coursework",
            "type": "ListItem"
        },
        {
            "element_id": "ea0a468e209c6995e8be6bc107b73c1c",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            216.1,
                            290.4
                        ],
                        [
                            216.1,
                            330.0
                        ],
                        [
                            333.1,
                            330.0
                        ],
                        [
                            333.1,
                            290.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 3,
                "parent_id": "8ee95aa06ba13e678ea9f5f597bd7285"
            },
            "text": "Principles of Marketing Internet Marketing Public Relations",
            "type": "Title"
        },
        {
            "element_id": "9c254109ad7bbfb9fb49b78e0cec769b",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            396.1,
                            290.4
                        ],
                        [
                            396.1,
                            330.0
                        ],
                        [
                            530.7,
                            330.0
                        ],
                        [
                            530.7,
                            290.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 3,
                "parent_id": "8ee95aa06ba13e678ea9f5f597bd7285"
            },
            "text": "Business Communication Consumer Behavior Business Policy & Stretegy",
            "type": "Title"
        },
        {
            "element_id": "3d6b06667ba03ea1b3c89faea71e130f",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            342.5
                        ],
                        [
                            72.0,
                            368.0
                        ],
                        [
                            134.4,
                            368.0
                        ],
                        [
                            134.4,
                            342.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 3,
                "parent_id": "9c254109ad7bbfb9fb49b78e0cec769b"
            },
            "text": "WORK HISTORY:",
            "type": "UncategorizedText"
        },
        {
            "element_id": "e18ee8bf2094c68e8883d7b21ef3eda9",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            180.0,
                            356.0
                        ],
                        [
                            180.0,
                            381.8
                        ],
                        [
                            357.7,
                            381.8
                        ],
                        [
                            357.7,
                            356.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 3,
                "parent_id": "8ee95aa06ba13e678ea9f5f597bd7285"
            },
            "text": "Aacademic Tutor (20xx to present) Bellevue University, Bellevue, NE",
            "type": "Title"
        },
        {
            "element_id": "4ef033d07b466526d29bbc792a06c90d",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            198.0,
                            384.5
                        ],
                        [
                            198.0,
                            410.3
                        ],
                        [
                            481.5,
                            410.3
                        ],
                        [
                            481.5,
                            384.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 3,
                "parent_id": "e18ee8bf2094c68e8883d7b21ef3eda9"
            },
            "text": "Assist college students in overcoming deficiencies and successfully mastering academic coursework.",
            "type": "ListItem"
        },
        {
            "element_id": "ef9de034f164076b451bc64e067435c4",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            180.0,
                            415.1
                        ],
                        [
                            180.0,
                            440.9
                        ],
                        [
                            420.3,
                            440.9
                        ],
                        [
                            420.3,
                            415.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 3,
                "parent_id": "8ee95aa06ba13e678ea9f5f597bd7285"
            },
            "text": "Senior Accounts Receivable Clerk (20xx-20xx) Lincoln Financial Group, Omaha, NE",
            "type": "Title"
        },
        {
            "element_id": "ecf471ae91516bed08184a3eb052b43c",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            198.0,
                            443.6
                        ],
                        [
                            198.0,
                            469.3
                        ],
                        [
                            509.8,
                            469.3
                        ],
                        [
                            509.8,
                            443.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 3,
                "parent_id": "ef9de034f164076b451bc64e067435c4"
            },
            "text": "Researched story ideas, wrote articles and participated in the publication of a weekly in-house newsletter.",
            "type": "ListItem"
        },
        {
            "element_id": "6d5a0b93030efb8007944adb2d4b950a",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            198.0,
                            472.0
                        ],
                        [
                            198.0,
                            497.8
                        ],
                        [
                            530.9,
                            497.8
                        ],
                        [
                            530.9,
                            472.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 3,
                "parent_id": "ef9de034f164076b451bc64e067435c4"
            },
            "text": "Assisted customers and staff members in resolving problems and balancing accounts; trained new staff members.",
            "type": "ListItem"
        },
        {
            "element_id": "abfaab172d34054fa0bc50c7a6ab2bfe",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            198.0,
                            500.4
                        ],
                        [
                            198.0,
                            526.2
                        ],
                        [
                            535.8,
                            526.2
                        ],
                        [
                            535.8,
                            500.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 3,
                "parent_id": "ef9de034f164076b451bc64e067435c4"
            },
            "text": "Managed and recorded daily accounts receivable deposits of up to $450,000.",
            "type": "ListItem"
        },
        {
            "element_id": "225facbadf44d77aaea471cd33fcabe0",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            198.0,
                            528.9
                        ],
                        [
                            198.0,
                            554.7
                        ],
                        [
                            540.1,
                            554.7
                        ],
                        [
                            540.1,
                            528.9
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 3,
                "parent_id": "ef9de034f164076b451bc64e067435c4"
            },
            "text": "Conducted extensive research to recover lost checks and organized system to stop payment and replace all checks.",
            "type": "ListItem"
        },
        {
            "element_id": "87b171fbb64d368f51d0f7135e1c2bcc",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            567.1
                        ],
                        [
                            72.0,
                            592.7
                        ],
                        [
                            157.3,
                            592.7
                        ],
                        [
                            157.3,
                            567.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 3,
                "parent_id": "ef9de034f164076b451bc64e067435c4"
            },
            "text": "COMMUNITY SERVICE:",
            "type": "UncategorizedText"
        },
        {
            "element_id": "9d062047249dd77987fe57b75239b969",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            180.0,
                            580.7
                        ],
                        [
                            180.0,
                            637.1
                        ],
                        [
                            440.7,
                            637.1
                        ],
                        [
                            440.7,
                            580.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 3,
                "parent_id": "ef9de034f164076b451bc64e067435c4"
            },
            "text": "Advertising Coordinator, The Vue (20xx to present) Bellevue University Student Newspaper Volunteer, Publicity Committee (20xx, 20xx) Brushup Nebraska Paint-A-Thon",
            "type": "UncategorizedText"
        },
        {
            "element_id": "209fc2c661d3b8c5bcd04db64eec0b0a",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            649.3
                        ],
                        [
                            72.0,
                            661.3
                        ],
                        [
                            405.4,
                            661.3
                        ],
                        [
                            405.4,
                            649.3
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 3,
                "parent_id": "8ee95aa06ba13e678ea9f5f597bd7285"
            },
            "text": "ADDED VALUE: Language Skills: Bilingual (English/Spanish)",
            "type": "Title"
        },
        {
            "element_id": "94b1750229a0da8f24e9eede99dcf656",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            180.0,
                            666.1
                        ],
                        [
                            180.0,
                            678.1
                        ],
                        [
                            517.1,
                            678.1
                        ],
                        [
                            517.1,
                            666.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 3,
                "parent_id": "8ee95aa06ba13e678ea9f5f597bd7285"
            },
            "text": "Computer Skills: MS Office (Word, Excel, PowerPoint), PhotoShop",
            "type": "Title"
        },
        {
            "element_id": "3dbca777dd0c557caef2b96100c96358",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            690.4
                        ],
                        [
                            72.0,
                            702.4
                        ],
                        [
                            159.7,
                            702.4
                        ],
                        [
                            159.7,
                            690.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 3,
                "parent_id": "94b1750229a0da8f24e9eede99dcf656"
            },
            "text": "REFERENCES:",
            "type": "UncategorizedText"
        },
        {
            "element_id": "0f8ea5a091856210c2bc86c2518f170c",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            180.0,
                            690.4
                        ],
                        [
                            180.0,
                            702.4
                        ],
                        [
                            307.0,
                            702.4
                        ],
                        [
                            307.0,
                            690.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 3,
                "parent_id": "8ee95aa06ba13e678ea9f5f597bd7285"
            },
            "text": "Available Upon Request",
            "type": "Title"
        },
        {
            "element_id": "b5c675ddf774acc9b0e97fadb93b25c9",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            410.9,
                            38.0
                        ],
                        [
                            410.9,
                            52.0
                        ],
                        [
                            543.3,
                            52.0
                        ],
                        [
                            543.3,
                            38.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 4
            },
            "text": "CHRONOLOGICAL",
            "type": "Header"
        },
        {
            "element_id": "006121cd05e59a4ea4835efe80c6f31e",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            247.2,
                            71.0
                        ],
                        [
                            247.2,
                            85.0
                        ],
                        [
                            368.3,
                            85.0
                        ],
                        [
                            368.3,
                            71.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 4,
                "parent_id": "b5c675ddf774acc9b0e97fadb93b25c9"
            },
            "text": "IM A. SAMPLE III",
            "type": "Title"
        },
        {
            "element_id": "2ddb6ba816aa94997a4104b18cec3f71",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            86.6
                        ],
                        [
                            72.0,
                            112.4
                        ],
                        [
                            202.0,
                            112.4
                        ],
                        [
                            202.0,
                            86.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 4,
                "parent_id": "b5c675ddf774acc9b0e97fadb93b25c9"
            },
            "text": "3456 Westview Road Bellevue, Nebraska 68005",
            "type": "Title"
        },
        {
            "element_id": "3826d43ae4da162e252a61c30c23804f",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            427.6,
                            86.6
                        ],
                        [
                            427.6,
                            112.4
                        ],
                        [
                            541.7,
                            112.4
                        ],
                        [
                            541.7,
                            86.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 4,
                "parent_id": "2ddb6ba816aa94997a4104b18cec3f71"
            },
            "text": "(402) 291-5678 imasample3@xxx.com",
            "type": "UncategorizedText"
        },
        {
            "element_id": "aa42191fd418edf14a4ccec08468d8e9",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            201.7,
                            128.6
                        ],
                        [
                            201.7,
                            141.5
                        ],
                        [
                            413.6,
                            141.5
                        ],
                        [
                            413.6,
                            128.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 4,
                "parent_id": "b5c675ddf774acc9b0e97fadb93b25c9"
            },
            "text": "SUMMARY OF QUALIFICATIONS",
            "type": "Title"
        },
        {
            "element_id": "dbe543e5eafe3b0a96b93d481d9e5fff",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            157.9
                        ],
                        [
                            72.0,
                            211.3
                        ],
                        [
                            543.1,
                            211.3
                        ],
                        [
                            543.1,
                            157.9
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 4,
                "parent_id": "aa42191fd418edf14a4ccec08468d8e9"
            },
            "text": "Experienced business professional with a solid academic background and a demonstrated commitment to providing high quality customer service; described as a \"take charge\" person with exceptional communication and human relations skills; proficient in the use of MS Office (Word, Excel, PowerPoint) with basic knowledge of PeopleSoft.",
            "type": "NarrativeText"
        },
        {
            "element_id": "f4bf852d0862192c5d4e63c2b6959b6b",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            269.3,
                            227.1
                        ],
                        [
                            269.3,
                            239.1
                        ],
                        [
                            345.7,
                            239.1
                        ],
                        [
                            345.7,
                            227.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 4,
                "parent_id": "b5c675ddf774acc9b0e97fadb93b25c9"
            },
            "text": "EDUCATION",
            "type": "Title"
        },
        {
            "element_id": "23624a01c68d19c92985c079905f7033",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            255.6
                        ],
                        [
                            72.0,
                            281.6
                        ],
                        [
                            368.1,
                            281.6
                        ],
                        [
                            368.1,
                            255.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 4,
                "parent_id": "f4bf852d0862192c5d4e63c2b6959b6b"
            },
            "text": "Bellevue University, Bellevue, NE (June 20xx) Bachelor of Science in Management of Human Resources",
            "type": "UncategorizedText"
        },
        {
            "element_id": "8540169d0ac13c2655cb5882f87721bd",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            284.1
                        ],
                        [
                            108.0,
                            296.2
                        ],
                        [
                            248.1,
                            296.2
                        ],
                        [
                            248.1,
                            284.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 4,
                "parent_id": "f4bf852d0862192c5d4e63c2b6959b6b"
            },
            "text": "GPA in major: 3.84/4.00",
            "type": "ListItem"
        },
        {
            "element_id": "e790bea546b6ec5bd4be563a34a2ac86",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            360.1,
                            284.2
                        ],
                        [
                            360.1,
                            296.2
                        ],
                        [
                            491.1,
                            296.2
                        ],
                        [
                            491.1,
                            284.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 4,
                "parent_id": "f4bf852d0862192c5d4e63c2b6959b6b"
            },
            "text": "Graduated with distinction",
            "type": "NarrativeText"
        },
        {
            "element_id": "dd988e3b3ee8fe6f96492a2dc2ff1b78",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            211.2,
                            312.2
                        ],
                        [
                            211.2,
                            325.2
                        ],
                        [
                            404.1,
                            325.2
                        ],
                        [
                            404.1,
                            312.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 4,
                "parent_id": "b5c675ddf774acc9b0e97fadb93b25c9"
            },
            "text": "PROFESSIONAL EXPERIENCE",
            "type": "Title"
        },
        {
            "element_id": "5ace91f16d36c9f09b8a857d78f598cf",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            340.4
                        ],
                        [
                            72.0,
                            366.2
                        ],
                        [
                            321.1,
                            366.2
                        ],
                        [
                            321.1,
                            340.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 4,
                "parent_id": "dd988e3b3ee8fe6f96492a2dc2ff1b78"
            },
            "text": "West Telemarketing, Omaha, NE (20xx to Present) Customer Service Supervisor (20xx to present)",
            "type": "UncategorizedText"
        },
        {
            "element_id": "9a9e75f34d29c2a625e3ba2165b44a91",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            368.0
                        ],
                        [
                            108.0,
                            407.6
                        ],
                        [
                            529.8,
                            407.6
                        ],
                        [
                            529.8,
                            368.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 4,
                "parent_id": "dd988e3b3ee8fe6f96492a2dc2ff1b78"
            },
            "text": "Supervise operations and staff in a 20-person inbound telemarketing unit, including hiring, training and evaluating employees, preparing and administering annual budgets, developing business plans, etc.",
            "type": "ListItem"
        },
        {
            "element_id": "728ad4e26345a4259439ed33d437c784",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            409.4
                        ],
                        [
                            108.0,
                            449.1
                        ],
                        [
                            536.4,
                            449.1
                        ],
                        [
                            536.4,
                            409.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 4,
                "parent_id": "dd988e3b3ee8fe6f96492a2dc2ff1b78"
            },
            "text": "Assess level of customer satisfaction and resolve sensitive and complex issues raised by customers; provide additional training and take other action as required to maintain a high level of customer satisfaction.",
            "type": "ListItem"
        },
        {
            "element_id": "0d91d4f71dde6ee902f3d55f568484ba",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            464.7
                        ],
                        [
                            72.0,
                            476.7
                        ],
                        [
                            308.7,
                            476.7
                        ],
                        [
                            308.7,
                            464.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 4,
                "parent_id": "b5c675ddf774acc9b0e97fadb93b25c9"
            },
            "text": "Customer Service Representative (20xx-20xx)",
            "type": "Title"
        },
        {
            "element_id": "895c881934a68dfb4b6191eeb4d70e89",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            478.5
                        ],
                        [
                            108.0,
                            490.5
                        ],
                        [
                            486.4,
                            490.5
                        ],
                        [
                            486.4,
                            478.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 4,
                "parent_id": "0d91d4f71dde6ee902f3d55f568484ba"
            },
            "text": "Handled incoming calls from customers and potential customers, provided",
            "type": "ListItem"
        },
        {
            "element_id": "4bf9a3ade18cf3458b0fc5db8f475b8d",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            506.7
                        ],
                        [
                            108.0,
                            517.9
                        ],
                        [
                            116.1,
                            517.9
                        ],
                        [
                            116.1,
                            506.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 4,
                "parent_id": "0d91d4f71dde6ee902f3d55f568484ba"
            },
            "text": "",
            "type": "ListItem"
        },
        {
            "element_id": "f5fa068155b2eb0d8b523fecefa42515",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            126.0,
                            492.3
                        ],
                        [
                            126.0,
                            531.9
                        ],
                        [
                            511.2,
                            531.9
                        ],
                        [
                            511.2,
                            492.3
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 4,
                "parent_id": "0d91d4f71dde6ee902f3d55f568484ba"
            },
            "text": "information and received orders using CRT to input data. Interviewed customers and recommended other available products to meet their needs; received several Incentive Awards for sales efforts.",
            "type": "NarrativeText"
        },
        {
            "element_id": "8665f89445e4eb56a329cb7f544a0c82",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            533.7
                        ],
                        [
                            108.0,
                            545.7
                        ],
                        [
                            397.6,
                            545.7
                        ],
                        [
                            397.6,
                            533.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 4,
                "parent_id": "0d91d4f71dde6ee902f3d55f568484ba"
            },
            "text": "Provided orientation and training to new staff members.",
            "type": "ListItem"
        },
        {
            "element_id": "dfe5e8f10bf3f021e66f7f9da4f93f73",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            151.2,
                            561.8
                        ],
                        [
                            151.2,
                            574.8
                        ],
                        [
                            464.0,
                            574.8
                        ],
                        [
                            464.0,
                            561.8
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 4,
                "parent_id": "b5c675ddf774acc9b0e97fadb93b25c9"
            },
            "text": "PROFESSIONAL AFFILIATIONS AND ACTIVITIES",
            "type": "Title"
        },
        {
            "element_id": "f7ff586ff3814f3b495e6aaa211f11c2",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            589.9
                        ],
                        [
                            72.0,
                            601.9
                        ],
                        [
                            453.6,
                            601.9
                        ],
                        [
                            453.6,
                            589.9
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 4,
                "parent_id": "b5c675ddf774acc9b0e97fadb93b25c9"
            },
            "text": "Member, Society for Human Resources Management (SHRM) (20xx to 20xx)",
            "type": "Title"
        },
        {
            "element_id": "b677005ebc8b15c306751cb4dba7ec47",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            603.7
                        ],
                        [
                            90.0,
                            615.7
                        ],
                        [
                            288.1,
                            615.7
                        ],
                        [
                            288.1,
                            603.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 4,
                "parent_id": "b5c675ddf774acc9b0e97fadb93b25c9"
            },
            "text": "Bellevue University Student Chapter",
            "type": "Title"
        },
        {
            "element_id": "ca9772300ae9a037bedb7d25406c84a4",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            617.6
                        ],
                        [
                            108.0,
                            629.6
                        ],
                        [
                            362.0,
                            629.6
                        ],
                        [
                            362.0,
                            617.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 4,
                "parent_id": "b677005ebc8b15c306751cb4dba7ec47"
            },
            "text": "Chair, Program Development Committee (20xx)",
            "type": "ListItem"
        },
        {
            "element_id": "7a45c4a2c815b47894644b77a517b45c",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            645.2
                        ],
                        [
                            72.0,
                            657.2
                        ],
                        [
                            458.5,
                            657.2
                        ],
                        [
                            458.5,
                            645.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 4,
                "parent_id": "b5c675ddf774acc9b0e97fadb93b25c9"
            },
            "text": "President, American Business Women's Association, Gold Star Chapter (20xx)",
            "type": "Title"
        },
        {
            "element_id": "2554dbbff3b41f6841fcf78da01e0af0",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            180.1,
                            674.2
                        ],
                        [
                            180.1,
                            686.2
                        ],
                        [
                            434.9,
                            686.2
                        ],
                        [
                            434.9,
                            674.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 4,
                "parent_id": "b5c675ddf774acc9b0e97fadb93b25c9"
            },
            "text": "REFERENCES FURNISHED UPON REQUEST",
            "type": "Title"
        },
        {
            "element_id": "bbf2be39a95661124449e07b563f2fc3",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            446.0,
                            38.0
                        ],
                        [
                            446.0,
                            52.0
                        ],
                        [
                            543.3,
                            52.0
                        ],
                        [
                            543.3,
                            38.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 5
            },
            "text": "FUNCTIONAL",
            "type": "Header"
        },
        {
            "element_id": "90d2c0804d25793384d0c426ee92f485",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            72.2
                        ],
                        [
                            72.0,
                            86.2
                        ],
                        [
                            195.6,
                            86.2
                        ],
                        [
                            195.6,
                            72.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 5,
                "parent_id": "bbf2be39a95661124449e07b563f2fc3"
            },
            "text": "IM A. SAMPLE IV",
            "type": "Title"
        },
        {
            "element_id": "46b9632d2d7b95298f5c9d8750a7531e",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            421.1,
                            87.7
                        ],
                        [
                            421.1,
                            141.1
                        ],
                        [
                            543.1,
                            141.1
                        ],
                        [
                            543.1,
                            87.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "links": [
                    {
                        "start_index": 58,
                        "text": "imasample4 @ xxx . com",
                        "url": "mailto:imasample4@xxx.com"
                    }
                ],
                "page_number": 5,
                "parent_id": "bbf2be39a95661124449e07b563f2fc3"
            },
            "text": "987 Northridge Drive Omaha, Nebraska 68123 (402) 543-1234 imasample4@xxx.com",
            "type": "Title"
        },
        {
            "element_id": "5ffe20535ab30c57bc944c00a4e1f85e",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            163.0
                        ],
                        [
                            72.0,
                            176.0
                        ],
                        [
                            528.2,
                            176.0
                        ],
                        [
                            528.2,
                            163.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 5,
                "parent_id": "46b9632d2d7b95298f5c9d8750a7531e"
            },
            "text": "OBJECTIVE: Position in market research or financial analysis where strong technical skills,",
            "type": "UncategorizedText"
        },
        {
            "element_id": "3b9703eea521c3d4aa986b497233a0f7",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            177.6
                        ],
                        [
                            108.0,
                            203.4
                        ],
                        [
                            539.8,
                            203.4
                        ],
                        [
                            539.8,
                            177.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 5,
                "parent_id": "46b9632d2d7b95298f5c9d8750a7531e"
            },
            "text": "mathematical/statistical background and problem solving abilities can be applied towards the successful achievement of business goals and objectives",
            "type": "NarrativeText"
        },
        {
            "element_id": "500168868c6b96583e640925524ecfd0",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            226.3
                        ],
                        [
                            72.0,
                            238.3
                        ],
                        [
                            224.7,
                            238.3
                        ],
                        [
                            224.7,
                            226.3
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 5,
                "parent_id": "bbf2be39a95661124449e07b563f2fc3"
            },
            "text": "PROFESSIONAL PROFILE",
            "type": "Title"
        },
        {
            "element_id": "70b23a160965e74321a2f3cee802239d",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            245.9
                        ],
                        [
                            90.0,
                            271.7
                        ],
                        [
                            539.3,
                            271.7
                        ],
                        [
                            539.3,
                            245.9
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 5,
                "parent_id": "500168868c6b96583e640925524ecfd0"
            },
            "text": "Exceptionally well organized, resourceful and highly motivated with the ability to handle multiple projects and produce timely, high quality work.",
            "type": "ListItem"
        },
        {
            "element_id": "b39dcb6baf417bedd23cc2ee7894545b",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            273.5
                        ],
                        [
                            90.0,
                            299.3
                        ],
                        [
                            523.5,
                            299.3
                        ],
                        [
                            523.5,
                            273.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 5,
                "parent_id": "500168868c6b96583e640925524ecfd0"
            },
            "text": "Strong analytical and human relations skills; especially effective in helping customers and associates resolve issues and concerns.",
            "type": "ListItem"
        },
        {
            "element_id": "1fdc462e7d5c0c8f0f1babd5b36692b7",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            310.6
                        ],
                        [
                            72.0,
                            322.6
                        ],
                        [
                            325.4,
                            322.6
                        ],
                        [
                            325.4,
                            310.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 5,
                "parent_id": "bbf2be39a95661124449e07b563f2fc3"
            },
            "text": "PROFESSIONAL SKILLS AND EXPERIENCE",
            "type": "Title"
        },
        {
            "element_id": "0d4fb98a88ced033980106f6a50a153f",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            330.4
                        ],
                        [
                            90.0,
                            355.9
                        ],
                        [
                            535.1,
                            355.9
                        ],
                        [
                            535.1,
                            330.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 5,
                "parent_id": "1fdc462e7d5c0c8f0f1babd5b36692b7"
            },
            "text": "Analysis and Problem Solving \uf0b7 Researched and developed a survey instrument, subsequently used to obtain information",
            "type": "NarrativeText"
        },
        {
            "element_id": "84de54b3a2a14d023c119ac6ed57697e",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            357.7
                        ],
                        [
                            108.0,
                            369.7
                        ],
                        [
                            441.1,
                            369.7
                        ],
                        [
                            441.1,
                            357.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 5,
                "parent_id": "1fdc462e7d5c0c8f0f1babd5b36692b7"
            },
            "text": "from customers regarding their satisfaction with products purchased.",
            "type": "NarrativeText"
        },
        {
            "element_id": "de1497569045e01e9e456c3d3c75ec7e",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            371.5
                        ],
                        [
                            90.0,
                            397.3
                        ],
                        [
                            539.3,
                            397.3
                        ],
                        [
                            539.3,
                            371.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 5,
                "parent_id": "1fdc462e7d5c0c8f0f1babd5b36692b7"
            },
            "text": "Compiled and analyzed statistical data to identify potential target markets for future sales and marketing efforts.",
            "type": "ListItem"
        },
        {
            "element_id": "400c5c3a5fe2f0c0f9fcfd4af28e3cdd",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            399.1
                        ],
                        [
                            90.0,
                            424.9
                        ],
                        [
                            536.2,
                            424.9
                        ],
                        [
                            536.2,
                            399.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 5,
                "parent_id": "1fdc462e7d5c0c8f0f1babd5b36692b7"
            },
            "text": "Completed independent research project on the use of mathematical/statistical models as tools for solving various business problems.",
            "type": "ListItem"
        },
        {
            "element_id": "9dfd04df13368b898337b0a883e487c4",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            426.7
                        ],
                        [
                            90.0,
                            452.5
                        ],
                        [
                            521.8,
                            452.5
                        ],
                        [
                            521.8,
                            426.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 5,
                "parent_id": "1fdc462e7d5c0c8f0f1babd5b36692b7"
            },
            "text": "Conducted quality control inspections, analyzed results and developed action plans to address areas of concern.",
            "type": "ListItem"
        },
        {
            "element_id": "83546d7391f7dfd9bd54897be121e6ac",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            454.6
                        ],
                        [
                            90.0,
                            480.1
                        ],
                        [
                            529.8,
                            480.1
                        ],
                        [
                            529.8,
                            454.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 5,
                "parent_id": "1fdc462e7d5c0c8f0f1babd5b36692b7"
            },
            "text": "Communications and Customer Relations \uf0b7 Received Customer Service Satisfaction Award for high quality of services provided to",
            "type": "NarrativeText"
        },
        {
            "element_id": "dee7327d69e50b2acb5a6b67b1da0e12",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            481.9
                        ],
                        [
                            108.0,
                            493.9
                        ],
                        [
                            248.4,
                            493.9
                        ],
                        [
                            248.4,
                            481.9
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 5,
                "parent_id": "bbf2be39a95661124449e07b563f2fc3"
            },
            "text": "both vendors and customers.",
            "type": "Title"
        },
        {
            "element_id": "91c9604cde85f3fea5613630be99aec3",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            495.7
                        ],
                        [
                            90.0,
                            521.5
                        ],
                        [
                            526.7,
                            521.5
                        ],
                        [
                            526.7,
                            495.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 5,
                "parent_id": "dee7327d69e50b2acb5a6b67b1da0e12"
            },
            "text": "Handled customer inquiries and sales; effectively represented company to vendors and prospective customers, resulting in a 15% increase in sales in just six months.",
            "type": "ListItem"
        },
        {
            "element_id": "4261862d69bc1a6d38e66850a96f12f1",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            523.3
                        ],
                        [
                            90.0,
                            535.3
                        ],
                        [
                            412.0,
                            535.3
                        ],
                        [
                            412.0,
                            523.3
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 5,
                "parent_id": "dee7327d69e50b2acb5a6b67b1da0e12"
            },
            "text": "Provided orientation, training and guidance to new employees.",
            "type": "ListItem"
        },
        {
            "element_id": "f10c6903a517bd5178b903a4a206f777",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            546.5
                        ],
                        [
                            72.0,
                            558.5
                        ],
                        [
                            148.3,
                            558.5
                        ],
                        [
                            148.3,
                            546.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 5,
                "parent_id": "bbf2be39a95661124449e07b563f2fc3"
            },
            "text": "EDUCATION",
            "type": "Title"
        },
        {
            "element_id": "b71d2c43d73714ae3cb9d48e8725f348",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            566.1
                        ],
                        [
                            90.0,
                            605.7
                        ],
                        [
                            429.1,
                            605.7
                        ],
                        [
                            429.1,
                            566.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 5,
                "parent_id": "f10c6903a517bd5178b903a4a206f777"
            },
            "text": "Bachelor of Science, Bellevue University, Bellevue, NE (June, 20xx) Major: Computer Information Systems in Business Graduated summa cum laude",
            "type": "UncategorizedText"
        },
        {
            "element_id": "18871643b53c626ef09a1116c09a674a",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            396.1,
                            579.9
                        ],
                        [
                            396.1,
                            605.7
                        ],
                        [
                            497.4,
                            605.7
                        ],
                        [
                            497.4,
                            579.9
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 5,
                "parent_id": "bbf2be39a95661124449e07b563f2fc3"
            },
            "text": "Minor: Mathematics GPA: 3.98/4.00",
            "type": "Title"
        },
        {
            "element_id": "ca660abddffd143aff0263dd9bdfe220",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            617.0
                        ],
                        [
                            72.0,
                            629.0
                        ],
                        [
                            194.1,
                            629.0
                        ],
                        [
                            194.1,
                            617.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 5,
                "parent_id": "bbf2be39a95661124449e07b563f2fc3"
            },
            "text": "TECHNICAL SKILLS",
            "type": "Title"
        },
        {
            "element_id": "4e6338994abf41d5049b20d151c73ffd",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            637.2
                        ],
                        [
                            90.0,
                            662.1
                        ],
                        [
                            98.1,
                            662.1
                        ],
                        [
                            98.1,
                            637.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 5,
                "parent_id": "ca660abddffd143aff0263dd9bdfe220"
            },
            "text": "\uf0b7",
            "type": "ListItem"
        },
        {
            "element_id": "00c5205d30b7fd675bb268bb1e760efc",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            636.5
                        ],
                        [
                            108.0,
                            662.3
                        ],
                        [
                            488.0,
                            662.3
                        ],
                        [
                            488.0,
                            636.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 5,
                "parent_id": "ca660abddffd143aff0263dd9bdfe220"
            },
            "text": "Java, PERL, ASP, PHP Scripting, Relational Databases, SQL Inferential Statistics, Data Analysis, Calculus & Mathematical Analysis, SPSS",
            "type": "UncategorizedText"
        },
        {
            "element_id": "374962237ef78448f97e2ac6b89f6288",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            673.6
                        ],
                        [
                            72.0,
                            685.6
                        ],
                        [
                            196.1,
                            685.6
                        ],
                        [
                            196.1,
                            673.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 5,
                "parent_id": "bbf2be39a95661124449e07b563f2fc3"
            },
            "text": "WORK EXPERIENCE",
            "type": "Title"
        },
        {
            "element_id": "4df9c78d2312916a843fa795e8974df0",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            693.2
                        ],
                        [
                            90.0,
                            719.0
                        ],
                        [
                            514.1,
                            719.0
                        ],
                        [
                            514.1,
                            693.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 5,
                "parent_id": "374962237ef78448f97e2ac6b89f6288"
            },
            "text": "Intern-Market Research, Mutual of Omaha, Omaha, NE (Fall Semester, 20xx) Sales Associate & Machinist Assistant, Precision Tool, Omaha, NE (20xx to present)",
            "type": "UncategorizedText"
        },
        {
            "element_id": "547c344383da87b2aaf1fd729702eec1",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            360.3,
                            38.0
                        ],
                        [
                            360.3,
                            52.0
                        ],
                        [
                            543.3,
                            52.0
                        ],
                        [
                            543.3,
                            38.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 6
            },
            "text": "FUNCTIONAL (MILITARY)",
            "type": "Header"
        },
        {
            "element_id": "16bb20a4e0d5f884b8027c20f054a744",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            71.0
                        ],
                        [
                            72.0,
                            85.0
                        ],
                        [
                            186.5,
                            85.0
                        ],
                        [
                            186.5,
                            71.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 6,
                "parent_id": "547c344383da87b2aaf1fd729702eec1"
            },
            "text": "IM A. SAMPLE V",
            "type": "Title"
        },
        {
            "element_id": "0a07b3decd71e6714547f03ae55383d3",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            421.1,
                            71.8
                        ],
                        [
                            421.1,
                            126.2
                        ],
                        [
                            543.1,
                            126.2
                        ],
                        [
                            543.1,
                            71.8
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 6,
                "parent_id": "547c344383da87b2aaf1fd729702eec1"
            },
            "text": "987 Northridge Drive Omaha, Nebraska 68123 (402) 543-1234 imasample5@xxx.com",
            "type": "Title"
        },
        {
            "element_id": "d1a2c12704ad118bfc016eadaf93ba5e",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            231.2,
                            155.1
                        ],
                        [
                            231.2,
                            167.1
                        ],
                        [
                            383.8,
                            167.1
                        ],
                        [
                            383.8,
                            155.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 6,
                "parent_id": "547c344383da87b2aaf1fd729702eec1"
            },
            "text": "PROFESSIONAL PROFILE",
            "type": "Title"
        },
        {
            "element_id": "15d95d79607e0c2859bd6bc74e2e98db",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            177.8
                        ],
                        [
                            72.0,
                            231.2
                        ],
                        [
                            542.3,
                            231.2
                        ],
                        [
                            542.3,
                            177.8
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 6,
                "parent_id": "d1a2c12704ad118bfc016eadaf93ba5e"
            },
            "text": "Self-motivated, resourceful and dynamic leader with extensive experience and a strong educational background in management, training and employee development; exceptional communication skills and a demonstrated ability to create and manage cohesive, productive work teams; proficient in the use of Microsoft Word, Excel and other software applications.",
            "type": "NarrativeText"
        },
        {
            "element_id": "1a9f027c64efb7840b6aff0865e0f569",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            157.5,
                            261.0
                        ],
                        [
                            157.5,
                            273.0
                        ],
                        [
                            457.5,
                            273.0
                        ],
                        [
                            457.5,
                            261.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 6,
                "parent_id": "547c344383da87b2aaf1fd729702eec1"
            },
            "text": "PROFESSIONAL SKILLS AND ACCOMPLISHMENTS",
            "type": "Title"
        },
        {
            "element_id": "5f691d0927c1583b8be1917cd93e3fb0",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            283.9
                        ],
                        [
                            72.0,
                            310.4
                        ],
                        [
                            530.6,
                            310.4
                        ],
                        [
                            530.6,
                            283.9
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 6,
                "parent_id": "1a9f027c64efb7840b6aff0865e0f569"
            },
            "text": "Management and Administration \uf0b7 Directed, guided and motivated a workforce of up to 300 individuals with diverse technical",
            "type": "NarrativeText"
        },
        {
            "element_id": "307895d26b0362fe5956c5cdf9f0f3d7",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            312.1
                        ],
                        [
                            90.0,
                            324.1
                        ],
                        [
                            237.4,
                            324.1
                        ],
                        [
                            237.4,
                            312.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 6,
                "parent_id": "547c344383da87b2aaf1fd729702eec1"
            },
            "text": "backgrounds and experiences.",
            "type": "Title"
        },
        {
            "element_id": "e2797548a0ecf192392f870d884e680f",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            326.8
                        ],
                        [
                            72.0,
                            395.8
                        ],
                        [
                            532.0,
                            395.8
                        ],
                        [
                            532.0,
                            326.8
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 6,
                "parent_id": "307895d26b0362fe5956c5cdf9f0f3d7"
            },
            "text": "Successfully improved work performance of a \u201cmarginal\u201d work team, as evidenced by an increase to a \u201csatisfactory\u201d performance rating after only six months as team leader. \uf0b7 Provided day-to-day supervision for an administrative staff of up to sixty employees. \uf0b7 Planned, designed and coordinated the programming of computer-based products; designed and coordinated computer system testing in facilities throughout the world.",
            "type": "ListItem"
        },
        {
            "element_id": "9b85986cffc77bb20b0a767591580137",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            398.4
                        ],
                        [
                            72.0,
                            410.5
                        ],
                        [
                            525.1,
                            410.5
                        ],
                        [
                            525.1,
                            398.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 6,
                "parent_id": "307895d26b0362fe5956c5cdf9f0f3d7"
            },
            "text": "Planned, developed and administered annual budgets ranging from $150,000 to $300,000.",
            "type": "ListItem"
        },
        {
            "element_id": "e79df92333ab8fc41f9c732bae6374b0",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            418.4
                        ],
                        [
                            72.0,
                            445.0
                        ],
                        [
                            540.0,
                            445.0
                        ],
                        [
                            540.0,
                            418.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 6,
                "parent_id": "307895d26b0362fe5956c5cdf9f0f3d7"
            },
            "text": "Training and Development \uf0b7 Taught college level courses in leadership, management, team building, effective writing and",
            "type": "UncategorizedText"
        },
        {
            "element_id": "469dd6aeeb885ba0c25024a15598c311",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            446.7
                        ],
                        [
                            90.0,
                            458.7
                        ],
                        [
                            211.0,
                            458.7
                        ],
                        [
                            211.0,
                            446.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 6,
                "parent_id": "547c344383da87b2aaf1fd729702eec1"
            },
            "text": "speech communications.",
            "type": "Title"
        },
        {
            "element_id": "491cd4d9a06eb361612885707d521f7f",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            461.3
                        ],
                        [
                            72.0,
                            487.1
                        ],
                        [
                            516.4,
                            487.1
                        ],
                        [
                            516.4,
                            461.3
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 6,
                "parent_id": "469dd6aeeb885ba0c25024a15598c311"
            },
            "text": "Certified as Master Instructor; designed and developed curriculum; selected, trained and evaluated other instructors.",
            "type": "ListItem"
        },
        {
            "element_id": "13e738384b06027412339883d0e722e6",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            489.8
                        ],
                        [
                            72.0,
                            515.7
                        ],
                        [
                            532.7,
                            515.7
                        ],
                        [
                            532.7,
                            489.8
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 6,
                "parent_id": "469dd6aeeb885ba0c25024a15598c311"
            },
            "text": "Advised and educated personnel on ways to enhance and strengthen their promotability and job performance; identified and documented career development plans for employees.",
            "type": "ListItem"
        },
        {
            "element_id": "54db094237f377eac93940e1b7a19136",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            518.3
                        ],
                        [
                            72.0,
                            530.4
                        ],
                        [
                            393.7,
                            530.4
                        ],
                        [
                            393.7,
                            518.3
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 6,
                "parent_id": "469dd6aeeb885ba0c25024a15598c311"
            },
            "text": "Provided on-the-job training and guidance for new employees.",
            "type": "ListItem"
        },
        {
            "element_id": "bd2c1a08cc79867b407572bc5d2a6f34",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            538.3
                        ],
                        [
                            72.0,
                            564.9
                        ],
                        [
                            496.1,
                            564.9
                        ],
                        [
                            496.1,
                            538.3
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 6,
                "parent_id": "469dd6aeeb885ba0c25024a15598c311"
            },
            "text": "Communication and Counseling \uf0b7 Conducted formal investigations and utilized a variety of counseling techniques and",
            "type": "NarrativeText"
        },
        {
            "element_id": "ab56d4ae6d891489062ed0acec908abc",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            566.5
                        ],
                        [
                            90.0,
                            592.3
                        ],
                        [
                            520.1,
                            592.3
                        ],
                        [
                            520.1,
                            566.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 6,
                "parent_id": "469dd6aeeb885ba0c25024a15598c311"
            },
            "text": "strategies to successfully resolve highly complex and sensitive issues involving domestic abuse, racial discrimination, minor law infractions and academic failures.",
            "type": "NarrativeText"
        },
        {
            "element_id": "c08231c838e0b3b15b05b5ff1ea1d669",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            595.0
                        ],
                        [
                            72.0,
                            620.8
                        ],
                        [
                            509.0,
                            620.8
                        ],
                        [
                            509.0,
                            595.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 6,
                "parent_id": "469dd6aeeb885ba0c25024a15598c311"
            },
            "text": "Worked one-on-one with customers and employees to enhance self esteem and resolve communication problems.",
            "type": "ListItem"
        },
        {
            "element_id": "4ba6cbec9939a31d474c5c1117746d13",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            623.5
                        ],
                        [
                            72.0,
                            649.3
                        ],
                        [
                            527.9,
                            649.3
                        ],
                        [
                            527.9,
                            623.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 6,
                "parent_id": "469dd6aeeb885ba0c25024a15598c311"
            },
            "text": "Marketed and promoted company programs to employees and the general public through a variety of activities including presentations to audiences of over 1000 people.",
            "type": "ListItem"
        },
        {
            "element_id": "ae2a2f5dfc8e9fad7cea61479aae4ac4",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            651.9
                        ],
                        [
                            72.0,
                            677.7
                        ],
                        [
                            528.8,
                            677.7
                        ],
                        [
                            528.8,
                            651.9
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 6,
                "parent_id": "469dd6aeeb885ba0c25024a15598c311"
            },
            "text": "Established and maintained effective working relationships with co-workers, superiors and subordinates to facilitate the achievement of business objectives.",
            "type": "ListItem"
        },
        {
            "element_id": "e3a04c1bc0640029fad7a1e8ac46522d",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            425.6,
                            701.2
                        ],
                        [
                            425.6,
                            711.2
                        ],
                        [
                            542.6,
                            711.2
                        ],
                        [
                            542.6,
                            701.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 6,
                "parent_id": "469dd6aeeb885ba0c25024a15598c311"
            },
            "text": "CONTINUED . . . . . . . . . . .",
            "type": "UncategorizedText"
        },
        {
            "element_id": "37869e22e8ed52b821d42a6c23435202",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            54.0
                        ],
                        [
                            72.0,
                            68.1
                        ],
                        [
                            186.3,
                            68.1
                        ],
                        [
                            186.3,
                            54.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 7,
                "parent_id": "547c344383da87b2aaf1fd729702eec1"
            },
            "text": "IM A. SAMPLE V",
            "type": "Title"
        },
        {
            "element_id": "9716a9082bed0aa086b95b0ee35f15ba",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            222.7,
                            97.5
                        ],
                        [
                            222.7,
                            109.5
                        ],
                        [
                            392.4,
                            109.5
                        ],
                        [
                            392.4,
                            97.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 7,
                "parent_id": "547c344383da87b2aaf1fd729702eec1"
            },
            "text": "EDUCATION AND TRAINING",
            "type": "Title"
        },
        {
            "element_id": "cff1a9cfa60350d33a5dd295e8789142",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            120.2
                        ],
                        [
                            72.0,
                            146.0
                        ],
                        [
                            293.4,
                            146.0
                        ],
                        [
                            293.4,
                            120.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 7,
                "parent_id": "547c344383da87b2aaf1fd729702eec1"
            },
            "text": "Bachelor of Science in Management (20xx) Bellevue University, Bellevue, Nebraska",
            "type": "Title"
        },
        {
            "element_id": "4303d81fa4fd6951ca231bd00cd5dd50",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            147.8
                        ],
                        [
                            108.0,
                            159.8
                        ],
                        [
                            186.7,
                            159.8
                        ],
                        [
                            186.7,
                            147.8
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 7,
                "parent_id": "cff1a9cfa60350d33a5dd295e8789142"
            },
            "text": "GPA: 4.00/4.00",
            "type": "UncategorizedText"
        },
        {
            "element_id": "1f9e26ee3618173894de90a35b8fb2d0",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            216.1,
                            147.8
                        ],
                        [
                            216.1,
                            159.8
                        ],
                        [
                            292.7,
                            159.8
                        ],
                        [
                            292.7,
                            147.8
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 7,
                "parent_id": "547c344383da87b2aaf1fd729702eec1"
            },
            "text": "Dean\u2019s Scholar",
            "type": "Title"
        },
        {
            "element_id": "f7fac18e3c1e74f108f72c375c95b845",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            324.1,
                            147.8
                        ],
                        [
                            324.1,
                            159.8
                        ],
                        [
                            502.2,
                            159.8
                        ],
                        [
                            502.2,
                            147.8
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 7,
                "parent_id": "547c344383da87b2aaf1fd729702eec1"
            },
            "text": "Graduated with Professional Honors",
            "type": "Title"
        },
        {
            "element_id": "16bfaa1ca145176a87cf2805d3614dde",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            170.9
                        ],
                        [
                            72.0,
                            196.7
                        ],
                        [
                            421.4,
                            196.7
                        ],
                        [
                            421.4,
                            170.9
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 7,
                "parent_id": "f7fac18e3c1e74f108f72c375c95b845"
            },
            "text": "Associate of Applied Science in Communications Technology (20xx) Community College of the Air Force",
            "type": "UncategorizedText"
        },
        {
            "element_id": "2c4f776963fa0a45140cda8b2721ac3d",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            207.7
                        ],
                        [
                            72.0,
                            247.3
                        ],
                        [
                            531.2,
                            247.3
                        ],
                        [
                            531.2,
                            207.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 7,
                "parent_id": "f7fac18e3c1e74f108f72c375c95b845"
            },
            "text": "Numerous workshops, courses and seminars dealing with leadership development, management, TQM, interpersonal communications, curriculum development and related topics Department of Defense and Air Force Training Schools",
            "type": "NarrativeText"
        },
        {
            "element_id": "9547b3bc3907d6bb82e2cf5818f15f0c",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            104.9,
                            258.2
                        ],
                        [
                            104.9,
                            284.0
                        ],
                        [
                            510.2,
                            284.0
                        ],
                        [
                            510.2,
                            258.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 7,
                "parent_id": "f7fac18e3c1e74f108f72c375c95b845"
            },
            "text": "Certified as Total Quality Management Facilitator Qualified Master Air Training Command Instructor in Leadership and Management",
            "type": "UncategorizedText"
        },
        {
            "element_id": "aa96eee16b625acfb938dc897bf5bfce",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            257.2,
                            313.8
                        ],
                        [
                            257.2,
                            325.8
                        ],
                        [
                            357.9,
                            325.8
                        ],
                        [
                            357.9,
                            313.8
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 7,
                "parent_id": "547c344383da87b2aaf1fd729702eec1"
            },
            "text": "WORK HISTORY",
            "type": "Title"
        },
        {
            "element_id": "2801ef5f7706a67331261e8aaebbc0e7",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            336.7
                        ],
                        [
                            72.0,
                            391.7
                        ],
                        [
                            393.9,
                            391.7
                        ],
                        [
                            393.9,
                            336.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 7,
                "parent_id": "aa96eee16b625acfb938dc897bf5bfce"
            },
            "text": "Various Positions of Increasing Responsibility and Leadership United States Air Force (20xx to present) \uf0b7 Currently serving as Squadron Operation Superintendent. \uf0b7 Scheduled to leave the Air Force in September 20xx.",
            "type": "NarrativeText"
        },
        {
            "element_id": "7aa8520f2212e1845e915cb373a9f409",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            198.5,
                            421.3
                        ],
                        [
                            198.5,
                            433.3
                        ],
                        [
                            416.6,
                            433.3
                        ],
                        [
                            416.6,
                            421.3
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 7,
                "parent_id": "547c344383da87b2aaf1fd729702eec1"
            },
            "text": "VOLUNTEER/COMMUNITY SERVICE",
            "type": "Title"
        },
        {
            "element_id": "6aea95b121be64047f57f3cb692d8801",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            444.1
                        ],
                        [
                            72.0,
                            469.9
                        ],
                        [
                            292.4,
                            469.9
                        ],
                        [
                            292.4,
                            444.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 7,
                "parent_id": "547c344383da87b2aaf1fd729702eec1"
            },
            "text": "Coach, Youth Soccer, Bellevue Boys Club Unit Coordinator, U.S. Savings Bond Drive",
            "type": "Title"
        },
        {
            "element_id": "adbaccb390cdd2fa0e9cfc7ef8d1b22e",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            179.8,
                            499.6
                        ],
                        [
                            179.8,
                            511.6
                        ],
                        [
                            435.3,
                            511.6
                        ],
                        [
                            435.3,
                            499.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 7,
                "parent_id": "547c344383da87b2aaf1fd729702eec1"
            },
            "text": "REFERENCES AVAILABLE UPON REQUEST",
            "type": "Title"
        },
        {
            "element_id": "a3954b7a1f5d3e43f23e9a6d6eb3edbf",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            486.1,
                            55.6
                        ],
                        [
                            486.1,
                            67.6
                        ],
                        [
                            542.4,
                            67.6
                        ],
                        [
                            542.4,
                            55.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 7,
                "parent_id": "547c344383da87b2aaf1fd729702eec1"
            },
            "text": "Page Two",
            "type": "Title"
        },
        {
            "element_id": "3e140ff449d0d863009f9156c2b2b7df",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            299.7,
                            38.0
                        ],
                        [
                            299.7,
                            52.0
                        ],
                        [
                            543.3,
                            52.0
                        ],
                        [
                            543.3,
                            38.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 8
            },
            "text": "CHRONOLOGICAL (MANAGERIAL)",
            "type": "Header"
        },
        {
            "element_id": "f9165eea9e399510e231d14f06083e0f",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            71.0
                        ],
                        [
                            72.0,
                            85.0
                        ],
                        [
                            192.2,
                            85.0
                        ],
                        [
                            192.2,
                            71.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 8,
                "parent_id": "3e140ff449d0d863009f9156c2b2b7df"
            },
            "text": "IM A. SAMPLE VI",
            "type": "Title"
        },
        {
            "element_id": "6322e21c816a1f6c347779c5b6d5d174",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            95.7
                        ],
                        [
                            72.0,
                            149.1
                        ],
                        [
                            193.9,
                            149.1
                        ],
                        [
                            193.9,
                            95.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 8,
                "parent_id": "3e140ff449d0d863009f9156c2b2b7df"
            },
            "text": "2345 Frederick Street Omaha, Nebraska 68123 (402) 489-3421 imasample6@xxx.com",
            "type": "Title"
        },
        {
            "element_id": "4e9c5b52a10f6858413edcddf420ecdd",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            218.6,
                            172.9
                        ],
                        [
                            218.6,
                            184.9
                        ],
                        [
                            395.6,
                            184.9
                        ],
                        [
                            395.6,
                            172.9
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 8,
                "parent_id": "3e140ff449d0d863009f9156c2b2b7df"
            },
            "text": "PROFESSIONAL HIGHLIGHTS",
            "type": "Title"
        },
        {
            "element_id": "bf7fb1ef4e7536ec0d660d39dd2b73ce",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            192.3
                        ],
                        [
                            72.0,
                            218.3
                        ],
                        [
                            528.0,
                            218.3
                        ],
                        [
                            528.0,
                            192.3
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 8,
                "parent_id": "4e9c5b52a10f6858413edcddf420ecdd"
            },
            "text": "\uf0d8 Extensive technical and management experience in information systems technology with a solid academic background in computer information systems and business administration.",
            "type": "UncategorizedText"
        },
        {
            "element_id": "aede8282bac315494b59c9114f5a9854",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            219.9
                        ],
                        [
                            72.0,
                            245.9
                        ],
                        [
                            511.1,
                            245.9
                        ],
                        [
                            511.1,
                            219.9
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 8,
                "parent_id": "4e9c5b52a10f6858413edcddf420ecdd"
            },
            "text": "\uf0d8 Excellent communicator with strong leadership skills and the ability to build cohesive, productive teams while fostering and encouraging creativity and individual expression.",
            "type": "NarrativeText"
        },
        {
            "element_id": "01ad482e26276d4366188385cef9bd2d",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            247.5
                        ],
                        [
                            72.0,
                            259.7
                        ],
                        [
                            183.6,
                            259.7
                        ],
                        [
                            183.6,
                            247.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 8,
                "parent_id": "3e140ff449d0d863009f9156c2b2b7df"
            },
            "text": "\uf0d8 Areas of expertise:",
            "type": "Title"
        },
        {
            "element_id": "23f9e96b03ddff25b2d3b01931291da5",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            261.5
                        ],
                        [
                            108.0,
                            301.0
                        ],
                        [
                            255.1,
                            301.0
                        ],
                        [
                            255.1,
                            261.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 8,
                "parent_id": "3e140ff449d0d863009f9156c2b2b7df"
            },
            "text": "Operations Management Mainframe & PC Operations Customer Relations",
            "type": "Title"
        },
        {
            "element_id": "23fc1b8c47f8bdce354e002584a378c3",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            288.1,
                            261.5
                        ],
                        [
                            288.1,
                            301.0
                        ],
                        [
                            402.1,
                            301.0
                        ],
                        [
                            402.1,
                            261.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 8,
                "parent_id": "3e140ff449d0d863009f9156c2b2b7df"
            },
            "text": "Project Management Software Development Technical Support",
            "type": "Title"
        },
        {
            "element_id": "cbbf38fe95433ae01b07d583d2a16235",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            432.1,
                            261.5
                        ],
                        [
                            432.1,
                            301.0
                        ],
                        [
                            536.7,
                            301.0
                        ],
                        [
                            536.7,
                            261.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 8,
                "parent_id": "3e140ff449d0d863009f9156c2b2b7df"
            },
            "text": "Quality Management Systems Design Troubleshooting",
            "type": "Title"
        },
        {
            "element_id": "f46378d6c9695a9474e2371a6ad8fe99",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            245.4,
                            312.2
                        ],
                        [
                            245.4,
                            324.2
                        ],
                        [
                            368.6,
                            324.2
                        ],
                        [
                            368.6,
                            312.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 8,
                "parent_id": "3e140ff449d0d863009f9156c2b2b7df"
            },
            "text": "WORK EXPERIENCE",
            "type": "Title"
        },
        {
            "element_id": "a76b9fd6335926c600690326bffc9d5d",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            331.8
                        ],
                        [
                            72.0,
                            371.4
                        ],
                        [
                            530.7,
                            371.4
                        ],
                        [
                            530.7,
                            331.8
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 8,
                "parent_id": "f46378d6c9695a9474e2371a6ad8fe99"
            },
            "text": "Supervisor, Financial Systems, Omaha Public Power District, Omaha NE (20xx to present) Oversee the maintenance and enhancement of financial systems to ensure process integrity and system stability for user areas.",
            "type": "NarrativeText"
        },
        {
            "element_id": "b1032c247cf4197c61d7ca7a8116b0e9",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            373.4
                        ],
                        [
                            72.0,
                            400.0
                        ],
                        [
                            540.9,
                            400.0
                        ],
                        [
                            540.9,
                            373.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 8,
                "parent_id": "f46378d6c9695a9474e2371a6ad8fe99"
            },
            "text": "Significant Accomplishments \uf0b7 Managed the implementation of a major software upgrade, significantly increasing efficiency",
            "type": "NarrativeText"
        },
        {
            "element_id": "e4ef17340e7ca9cbcce8743361c0c373",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            401.6
                        ],
                        [
                            90.0,
                            413.6
                        ],
                        [
                            357.4,
                            413.6
                        ],
                        [
                            357.4,
                            401.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 8,
                "parent_id": "f46378d6c9695a9474e2371a6ad8fe99"
            },
            "text": "in the use of accounts payable and purchasing systems.",
            "type": "NarrativeText"
        },
        {
            "element_id": "72bb8efba327a20dd7e3febab2364342",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            416.3
                        ],
                        [
                            72.0,
                            456.9
                        ],
                        [
                            538.9,
                            456.9
                        ],
                        [
                            538.9,
                            416.3
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 8,
                "parent_id": "f46378d6c9695a9474e2371a6ad8fe99"
            },
            "text": "Converted contract and payee information from a third party system to an internal automated system, resulting in approximately $72,000 in annual revenue for the organization. \uf0b7 Developed a cohesive, productive work team of individuals from diverse areas of the",
            "type": "ListItem"
        },
        {
            "element_id": "f3fb458b583165f15f72383d23ceac8c",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            458.7
                        ],
                        [
                            90.0,
                            484.5
                        ],
                        [
                            513.6,
                            484.5
                        ],
                        [
                            513.6,
                            458.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 8,
                "parent_id": "f46378d6c9695a9474e2371a6ad8fe99"
            },
            "text": "organization, utilizing strong interpersonal and leadership skills to foster and encourage teamwork and cooperation among team members and with user areas.",
            "type": "NarrativeText"
        },
        {
            "element_id": "0607664985d9bc0a33b338336130889d",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            487.1
                        ],
                        [
                            72.0,
                            512.9
                        ],
                        [
                            512.4,
                            512.9
                        ],
                        [
                            512.4,
                            487.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 8,
                "parent_id": "f46378d6c9695a9474e2371a6ad8fe99"
            },
            "text": "Utilized TQM principles to implement several internal process improvements that have resulted in hundreds of time-saving hours annually.",
            "type": "ListItem"
        },
        {
            "element_id": "c22e01f5b75d3f0fe0db1cfbce50cf09",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            515.6
                        ],
                        [
                            72.0,
                            527.7
                        ],
                        [
                            479.7,
                            527.7
                        ],
                        [
                            479.7,
                            515.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 8,
                "parent_id": "f46378d6c9695a9474e2371a6ad8fe99"
            },
            "text": "Promoted into management position after only six months as a Systems Analyst.",
            "type": "ListItem"
        },
        {
            "element_id": "1f389d9d76f4a1813d56198578d0429b",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            538.6
                        ],
                        [
                            72.0,
                            564.4
                        ],
                        [
                            470.0,
                            564.4
                        ],
                        [
                            470.0,
                            538.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 8,
                "parent_id": "f46378d6c9695a9474e2371a6ad8fe99"
            },
            "text": "Programmer/Analyst, Bishop Clarkson Hospital, Omaha NE (20xx \u2013 20xx) Provided systems support and enhancements to user areas throughout the hospital.",
            "type": "NarrativeText"
        },
        {
            "element_id": "ae5c062889ace2cdffbeaa5ab86b01b6",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            566.4
                        ],
                        [
                            72.0,
                            592.9
                        ],
                        [
                            535.1,
                            592.9
                        ],
                        [
                            535.1,
                            566.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 8,
                "parent_id": "f46378d6c9695a9474e2371a6ad8fe99"
            },
            "text": "Significant Accomplishments \uf0b7 Developed and implemented an automated system for processing employee timesheets, thus",
            "type": "NarrativeText"
        },
        {
            "element_id": "b81b62b1155c040dc176b35e1a482c0b",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            594.6
                        ],
                        [
                            90.0,
                            606.6
                        ],
                        [
                            325.0,
                            606.6
                        ],
                        [
                            325.0,
                            594.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 8,
                "parent_id": "f46378d6c9695a9474e2371a6ad8fe99"
            },
            "text": "eliminating the need for handwritten timesheets.",
            "type": "NarrativeText"
        },
        {
            "element_id": "916765834fa9a2ca1c2b466764b642d1",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            609.3
                        ],
                        [
                            72.0,
                            635.1
                        ],
                        [
                            494.8,
                            635.1
                        ],
                        [
                            494.8,
                            609.3
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 8,
                "parent_id": "f46378d6c9695a9474e2371a6ad8fe99"
            },
            "text": "Researched, designed and developed a new software application now being used by managers throughout the organization for strategic planning and reporting.",
            "type": "ListItem"
        },
        {
            "element_id": "279428aef46f2e7db4b4b7320dc9ced2",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            637.7
                        ],
                        [
                            72.0,
                            663.5
                        ],
                        [
                            529.7,
                            663.5
                        ],
                        [
                            529.7,
                            637.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 8,
                "parent_id": "f46378d6c9695a9474e2371a6ad8fe99"
            },
            "text": "Recognized as Information Systems Employee of the Year for the high quality of customer service provided and the successful resolution of numerous systems problems.",
            "type": "ListItem"
        },
        {
            "element_id": "4c6ebb1e301608bf302163210f2b5ccf",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            475.9,
                            686.9
                        ],
                        [
                            475.9,
                            695.9
                        ],
                        [
                            542.4,
                            695.9
                        ],
                        [
                            542.4,
                            686.9
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 8,
                "parent_id": "3e140ff449d0d863009f9156c2b2b7df"
            },
            "text": "Page One of Two",
            "type": "Title"
        },
        {
            "element_id": "fc939817a74017f26f718d4a6468c4de",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            53.8
                        ],
                        [
                            72.0,
                            67.8
                        ],
                        [
                            540.0,
                            67.8
                        ],
                        [
                            540.0,
                            53.8
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 9,
                "parent_id": "4c6ebb1e301608bf302163210f2b5ccf"
            },
            "text": "IM A. SAMPLE VI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Page Two of Two",
            "type": "UncategorizedText"
        },
        {
            "element_id": "a05f2f376ba0664394bcf09d8ce5eea1",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            212.9,
                            91.5
                        ],
                        [
                            212.9,
                            103.5
                        ],
                        [
                            402.1,
                            103.5
                        ],
                        [
                            402.1,
                            91.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 9,
                "parent_id": "3e140ff449d0d863009f9156c2b2b7df"
            },
            "text": "WORK EXPERIENCE (Continued)",
            "type": "Title"
        },
        {
            "element_id": "8d600ba56ad48ce5d08e978d39e86453",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            114.2
                        ],
                        [
                            72.0,
                            141.0
                        ],
                        [
                            514.7,
                            141.0
                        ],
                        [
                            514.7,
                            114.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 9,
                "parent_id": "a05f2f376ba0664394bcf09d8ce5eea1"
            },
            "text": "Senior Computer Operator, Bergen Mercy Hospital, Omaha NE (20xx \u2013 20xx) \uf0b7 Supervised shift operations and staff, trained employees, developed work schedules and",
            "type": "NarrativeText"
        },
        {
            "element_id": "9085bf5c89c17a96d14e4efc8e81c051",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            142.8
                        ],
                        [
                            90.0,
                            154.8
                        ],
                        [
                            236.7,
                            154.8
                        ],
                        [
                            236.7,
                            142.8
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 9,
                "parent_id": "3e140ff449d0d863009f9156c2b2b7df"
            },
            "text": "monitored work performance.",
            "type": "Title"
        },
        {
            "element_id": "4d001e9e6b1ff6e9406d081eecbd5541",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            157.4
                        ],
                        [
                            72.0,
                            183.2
                        ],
                        [
                            528.0,
                            183.2
                        ],
                        [
                            528.0,
                            157.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 9,
                "parent_id": "9085bf5c89c17a96d14e4efc8e81c051"
            },
            "text": "Operated IBM and Digital systems; identified and resolved problems to assure smooth and efficient system operations.",
            "type": "ListItem"
        },
        {
            "element_id": "d81dd058d776e0edbcf75498946cd9c3",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            269.3,
                            194.4
                        ],
                        [
                            269.3,
                            206.4
                        ],
                        [
                            344.7,
                            206.4
                        ],
                        [
                            344.7,
                            194.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 9,
                "parent_id": "3e140ff449d0d863009f9156c2b2b7df"
            },
            "text": "EDUCATION",
            "type": "Title"
        },
        {
            "element_id": "7f44f101af84edc6565a0b3a74b4dced",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            214.2
                        ],
                        [
                            72.0,
                            239.7
                        ],
                        [
                            399.1,
                            239.7
                        ],
                        [
                            399.1,
                            214.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 9,
                "parent_id": "3e140ff449d0d863009f9156c2b2b7df"
            },
            "text": "MBA with Concentration in Management Information Systems Bellevue University, Bellevue NE",
            "type": "Title"
        },
        {
            "element_id": "4a69694f25baa9e0ceddd6e466bcc965",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            360.1,
                            227.7
                        ],
                        [
                            360.1,
                            239.7
                        ],
                        [
                            520.1,
                            239.7
                        ],
                        [
                            520.1,
                            227.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 9,
                "parent_id": "3e140ff449d0d863009f9156c2b2b7df"
            },
            "text": "Expected Graduation: June 20xx",
            "type": "Title"
        },
        {
            "element_id": "9bd5dbce0cd75dc65d42a69748d7ba6b",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            250.8
                        ],
                        [
                            72.0,
                            262.8
                        ],
                        [
                            380.0,
                            262.8
                        ],
                        [
                            380.0,
                            250.8
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 9,
                "parent_id": "3e140ff449d0d863009f9156c2b2b7df"
            },
            "text": "Bachelor of Science, Bellevue University, Bellevue NE (20xx)",
            "type": "Title"
        },
        {
            "element_id": "b0574b90e29b7cb5252a4cc16b8a3c6f",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            264.6
                        ],
                        [
                            108.0,
                            290.4
                        ],
                        [
                            298.0,
                            290.4
                        ],
                        [
                            298.0,
                            264.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 9,
                "parent_id": "3e140ff449d0d863009f9156c2b2b7df"
            },
            "text": "Major: Computer Information Systems GPA: 3.45/4.00",
            "type": "Title"
        },
        {
            "element_id": "5d361642352b0006a90dba7df0a9b177",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            216.1,
                            278.4
                        ],
                        [
                            216.1,
                            290.4
                        ],
                        [
                            338.1,
                            290.4
                        ],
                        [
                            338.1,
                            278.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 9,
                "parent_id": "3e140ff449d0d863009f9156c2b2b7df"
            },
            "text": "GPA in major: 4.00/4.00",
            "type": "Title"
        },
        {
            "element_id": "08cf2127d1a2b27269aaa16a9f8d7fff",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            360.1,
                            264.6
                        ],
                        [
                            360.1,
                            290.4
                        ],
                        [
                            517.8,
                            290.4
                        ],
                        [
                            517.8,
                            264.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 9,
                "parent_id": "3e140ff449d0d863009f9156c2b2b7df"
            },
            "text": "Minor: Business Administration Dean\u2019s Scholar",
            "type": "Title"
        },
        {
            "element_id": "078d45bb482d4b5b3c443bc40ea89c1a",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            301.7
                        ],
                        [
                            72.0,
                            327.2
                        ],
                        [
                            381.3,
                            327.2
                        ],
                        [
                            381.3,
                            301.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 9,
                "parent_id": "3e140ff449d0d863009f9156c2b2b7df"
            },
            "text": "Certificate in Computer Programming Electronic Computer Programming Institute, Omaha NE (20xx)",
            "type": "Title"
        },
        {
            "element_id": "d4af5225fe52b7018eb8a6b88311f1e4",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            189.7,
                            338.4
                        ],
                        [
                            189.7,
                            350.4
                        ],
                        [
                            424.2,
                            350.4
                        ],
                        [
                            424.2,
                            338.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 9,
                "parent_id": "3e140ff449d0d863009f9156c2b2b7df"
            },
            "text": "TECHNICAL KNOWLEDGE AND SKILLS",
            "type": "Title"
        },
        {
            "element_id": "736bbeab3e3efe355c9f7f74eda5bfa0",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            358.0
                        ],
                        [
                            108.0,
                            411.4
                        ],
                        [
                            327.1,
                            411.4
                        ],
                        [
                            327.1,
                            358.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 9,
                "parent_id": "d4af5225fe52b7018eb8a6b88311f1e4"
            },
            "text": "C, C++, Visual Basic, COBOL Advanced Microcomputer Applications Management & Design of Database Systems Relational Database Management",
            "type": "UncategorizedText"
        },
        {
            "element_id": "7a3d081fffe256b735f82bf7fec9e829",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            360.1,
                            358.0
                        ],
                        [
                            360.1,
                            411.4
                        ],
                        [
                            530.7,
                            411.4
                        ],
                        [
                            530.7,
                            358.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 9,
                "parent_id": "3e140ff449d0d863009f9156c2b2b7df"
            },
            "text": "Windows 9x/200x/XP UNIX/Linux SQL Microcomputer Graphics/Mapping",
            "type": "Title"
        },
        {
            "element_id": "eb17d140f804383217180456895e3bcb",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            171.0,
                            413.2
                        ],
                        [
                            171.0,
                            425.2
                        ],
                        [
                            444.1,
                            425.2
                        ],
                        [
                            444.1,
                            413.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 9,
                "parent_id": "3e140ff449d0d863009f9156c2b2b7df"
            },
            "text": "MS Office (Word, Excel, PowerPoint, Outlook, Access)",
            "type": "Title"
        },
        {
            "element_id": "0ac3928309c12abca8dc5d8284b5ea31",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            179.8,
                            448.9
                        ],
                        [
                            179.8,
                            460.9
                        ],
                        [
                            435.3,
                            460.9
                        ],
                        [
                            435.3,
                            448.9
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 9,
                "parent_id": "3e140ff449d0d863009f9156c2b2b7df"
            },
            "text": "REFERENCES AVAILABLE UPON REQUEST",
            "type": "Title"
        },
        {
            "element_id": "7a44e99423f434d3cd1f9f97085eda74",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            203.9,
                            38.0
                        ],
                        [
                            203.9,
                            52.0
                        ],
                        [
                            543.6,
                            52.0
                        ],
                        [
                            543.6,
                            38.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 10
            },
            "text": "CHRONOLOGICAL (GRADUATE ASSISTANTSHIP)",
            "type": "Header"
        },
        {
            "element_id": "b641fb6b17721c36c4971fc9d605abe5",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            245.6,
                            64.9
                        ],
                        [
                            245.6,
                            131.9
                        ],
                        [
                            369.6,
                            131.9
                        ],
                        [
                            369.6,
                            64.9
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "links": [
                    {
                        "start_index": 77,
                        "text": "imasample7 @ xxx . com",
                        "url": "mailto:imasample7@xxx.com"
                    }
                ],
                "page_number": 10,
                "parent_id": "7a44e99423f434d3cd1f9f97085eda74"
            },
            "text": "IM A. SAMPLE VII 4321 Country Club Road Omaha, Nebraska 68123 (402) 555-9876 imasample7@xxx.com",
            "type": "UncategorizedText"
        },
        {
            "element_id": "3ab993a721e343784fb3eae2ae9a3380",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            271.4,
                            147.7
                        ],
                        [
                            271.4,
                            159.7
                        ],
                        [
                            343.8,
                            159.7
                        ],
                        [
                            343.8,
                            147.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 10,
                "parent_id": "7a44e99423f434d3cd1f9f97085eda74"
            },
            "text": "OBJECTIVE",
            "type": "Title"
        },
        {
            "element_id": "f228d6b556534fdcc3c7f18e4e7adc3e",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            82.8,
                            170.5
                        ],
                        [
                            82.8,
                            196.3
                        ],
                        [
                            532.2,
                            196.3
                        ],
                        [
                            532.2,
                            170.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 10,
                "parent_id": "3ab993a721e343784fb3eae2ae9a3380"
            },
            "text": "To obtain a Graduate Assistantship where strong academic background and excellent communication skills can be utilized to help college students achieve their educational goals.",
            "type": "NarrativeText"
        },
        {
            "element_id": "e54c9a24e93275beb2f9f7bdda6b36e9",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            269.3,
                            212.1
                        ],
                        [
                            269.3,
                            224.1
                        ],
                        [
                            345.7,
                            224.1
                        ],
                        [
                            345.7,
                            212.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 10,
                "parent_id": "7a44e99423f434d3cd1f9f97085eda74"
            },
            "text": "EDUCATION",
            "type": "Title"
        },
        {
            "element_id": "694b04ed8060f6197b4c90f87cd745c8",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            234.9
                        ],
                        [
                            72.0,
                            246.9
                        ],
                        [
                            364.6,
                            246.9
                        ],
                        [
                            364.6,
                            234.9
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 10,
                "parent_id": "7a44e99423f434d3cd1f9f97085eda74"
            },
            "text": "Bachelor of Arts, Bellevue University, Bellevue NE (20xx)",
            "type": "Title"
        },
        {
            "element_id": "01e55306ec7e3622a703e94c6f2a8581",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            248.7
                        ],
                        [
                            108.0,
                            274.6
                        ],
                        [
                            262.1,
                            274.6
                        ],
                        [
                            262.1,
                            248.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 10,
                "parent_id": "7a44e99423f434d3cd1f9f97085eda74"
            },
            "text": "Majors: Psychology, Sociology Graduated Summa Cum Laude",
            "type": "Title"
        },
        {
            "element_id": "c7ff67a0078ba1938eae3b0142594f22",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            250.2,
                            262.6
                        ],
                        [
                            250.2,
                            288.6
                        ],
                        [
                            364.9,
                            288.6
                        ],
                        [
                            364.9,
                            262.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 10,
                "parent_id": "7a44e99423f434d3cd1f9f97085eda74"
            },
            "text": "Dean\u2019s Scholar Relevant Coursework",
            "type": "Title"
        },
        {
            "element_id": "c761161a25421392c3e22b5b9a1e8deb",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            396.1,
                            248.7
                        ],
                        [
                            396.1,
                            274.6
                        ],
                        [
                            499.1,
                            274.6
                        ],
                        [
                            499.1,
                            248.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 10,
                "parent_id": "7a44e99423f434d3cd1f9f97085eda74"
            },
            "text": "GPA: 4.00/4.00 National Dean\u2019s List",
            "type": "Title"
        },
        {
            "element_id": "1dc69747cf4d26b3796164470f3d8002",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            290.2
                        ],
                        [
                            108.0,
                            329.8
                        ],
                        [
                            329.7,
                            329.8
                        ],
                        [
                            329.7,
                            290.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 10,
                "parent_id": "7a44e99423f434d3cd1f9f97085eda74"
            },
            "text": "Fundamentals of Guidance & Counseling Psychological Assessment Research Methods & Psychological Research",
            "type": "Title"
        },
        {
            "element_id": "cb0bd56b938953d8505d1ec2a4bd8eb3",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            396.1,
                            290.2
                        ],
                        [
                            396.1,
                            329.8
                        ],
                        [
                            490.8,
                            329.8
                        ],
                        [
                            490.8,
                            290.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 10,
                "parent_id": "7a44e99423f434d3cd1f9f97085eda74"
            },
            "text": "Personality Theory Learning Theory Social Psychology",
            "type": "Title"
        },
        {
            "element_id": "c25043d857237ca5ef6159ffcee4bbe6",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            218.4,
                            345.6
                        ],
                        [
                            218.4,
                            357.6
                        ],
                        [
                            396.6,
                            357.6
                        ],
                        [
                            396.6,
                            345.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 10,
                "parent_id": "7a44e99423f434d3cd1f9f97085eda74"
            },
            "text": "PROFESSIONAL EXPERIENCE",
            "type": "Title"
        },
        {
            "element_id": "920954ad647849506339ae908e6726a5",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            368.3
                        ],
                        [
                            72.0,
                            395.0
                        ],
                        [
                            531.7,
                            395.0
                        ],
                        [
                            531.7,
                            368.3
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 10,
                "parent_id": "c25043d857237ca5ef6159ffcee4bbe6"
            },
            "text": "Writing Tutor and Test Administrator, Bellevue University, Bellevue, NE (20xx \u2013 20xx) \uf0b7 Assisted in the preparation and administration of various assessment instruments, including",
            "type": "NarrativeText"
        },
        {
            "element_id": "7b410cc7eef0d6e8aeb82366a30f9889",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            396.7
                        ],
                        [
                            90.0,
                            408.7
                        ],
                        [
                            275.8,
                            408.7
                        ],
                        [
                            275.8,
                            396.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 10,
                "parent_id": "7a44e99423f434d3cd1f9f97085eda74"
            },
            "text": "CLEP, DANTES and placement tests.",
            "type": "Title"
        },
        {
            "element_id": "cd34e3fae0275a06c91f36e73ecea11b",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            411.4
                        ],
                        [
                            72.0,
                            437.3
                        ],
                        [
                            481.6,
                            437.3
                        ],
                        [
                            481.6,
                            411.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 10,
                "parent_id": "7b410cc7eef0d6e8aeb82366a30f9889"
            },
            "text": "Provided tutorial assistance to undergraduate and graduate students in the area of writing/composition.",
            "type": "ListItem"
        },
        {
            "element_id": "37c87b5c84f1de3ac6b20554fc2e716a",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            440.0
                        ],
                        [
                            72.0,
                            465.7
                        ],
                        [
                            539.2,
                            465.7
                        ],
                        [
                            539.2,
                            440.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 10,
                "parent_id": "7b410cc7eef0d6e8aeb82366a30f9889"
            },
            "text": "Advised and assisted international students with writing assignments to help them strengthen their English language skills.",
            "type": "ListItem"
        },
        {
            "element_id": "1746acf2ef0adc286619ca40491676f6",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            470.5
                        ],
                        [
                            72.0,
                            497.3
                        ],
                        [
                            538.7,
                            497.3
                        ],
                        [
                            538.7,
                            470.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 10,
                "parent_id": "7b410cc7eef0d6e8aeb82366a30f9889"
            },
            "text": "Research Assistant, University of Nebraska Medical Center, Omaha, NE (Summer 20xx, 20xx) \uf0b7 Assisted child psychologist in a two-part Summer Research Enrichment Program, including",
            "type": "UncategorizedText"
        },
        {
            "element_id": "4adb98017f36249f5b43cbfda3c8a0e2",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            499.0
                        ],
                        [
                            90.0,
                            511.0
                        ],
                        [
                            468.2,
                            511.0
                        ],
                        [
                            468.2,
                            499.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 10,
                "parent_id": "7a44e99423f434d3cd1f9f97085eda74"
            },
            "text": "observations of client behavior, data entry and preparation of research reports.",
            "type": "Title"
        },
        {
            "element_id": "c9ad098356aec79a6037289a597fe383",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            513.6
                        ],
                        [
                            72.0,
                            539.4
                        ],
                        [
                            518.1,
                            539.4
                        ],
                        [
                            518.1,
                            513.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 10,
                "parent_id": "4adb98017f36249f5b43cbfda3c8a0e2"
            },
            "text": "Performed literature searches and prepared summary reports for a major research project involving the study of individuals with disabilities.",
            "type": "ListItem"
        },
        {
            "element_id": "8ea98cbb212a7828224a60dc4d1fd781",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            186.7,
                            555.3
                        ],
                        [
                            186.7,
                            567.3
                        ],
                        [
                            428.2,
                            567.3
                        ],
                        [
                            428.2,
                            555.3
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 10,
                "parent_id": "7a44e99423f434d3cd1f9f97085eda74"
            },
            "text": "COLLEGIATE HONORS AND ACTIVITIES",
            "type": "Title"
        },
        {
            "element_id": "434fe6f03beceaed81e33298895d857b",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            578.1
                        ],
                        [
                            72.0,
                            657.3
                        ],
                        [
                            488.4,
                            657.3
                        ],
                        [
                            488.4,
                            578.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 10,
                "parent_id": "8ea98cbb212a7828224a60dc4d1fd781"
            },
            "text": "Listed in Who\u2019s Who Among Students in American Colleges and Universities Member, Pi Gamma Mu and Alpha Chi Honor Societies President, Behavioral and Social Sciences Student Organization, Bellevue University Volunteer Contributor, The VUE, Bellevue University Student Newspaper Member, Bellevue University Student Advisory Council",
            "type": "UncategorizedText"
        },
        {
            "element_id": "2aa2b298931f168fe2bcb4bc3db3ae2c",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            148.5,
                            673.1
                        ],
                        [
                            148.5,
                            685.1
                        ],
                        [
                            466.6,
                            685.1
                        ],
                        [
                            466.6,
                            673.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 10,
                "parent_id": "7a44e99423f434d3cd1f9f97085eda74"
            },
            "text": "LETTERS OF REFERENCE & TRANSCRIPT ENCLOSED",
            "type": "Title"
        },
        {
            "element_id": "868242aff5ab9e45675f6ad08748e4e9",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            227.8,
                            38.0
                        ],
                        [
                            227.8,
                            52.0
                        ],
                        [
                            543.6,
                            52.0
                        ],
                        [
                            543.6,
                            38.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 11
            },
            "text": "CHRONOLOGICAL (COMPUTER/TECHNICAL)",
            "type": "Header"
        },
        {
            "element_id": "2b7261647dd4305aebdae3d5d32bcb2f",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            233.1,
                            74.4
                        ],
                        [
                            233.1,
                            145.2
                        ],
                        [
                            382.9,
                            145.2
                        ],
                        [
                            382.9,
                            74.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 11,
                "parent_id": "868242aff5ab9e45675f6ad08748e4e9"
            },
            "text": "IM A. SAMPLE VIII 5432 North 97 Street Omaha, Nebraska 68134 (402) 493-1234 imasample8@xxx.com",
            "type": "UncategorizedText"
        },
        {
            "element_id": "34472c1c0daadade232ef7d1e2825394",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            271.4,
                            167.1
                        ],
                        [
                            271.4,
                            179.1
                        ],
                        [
                            343.8,
                            179.1
                        ],
                        [
                            343.8,
                            167.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 11,
                "parent_id": "868242aff5ab9e45675f6ad08748e4e9"
            },
            "text": "OBJECTIVE",
            "type": "Title"
        },
        {
            "element_id": "02b1b945178fdda147255ae046949144",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            186.7
                        ],
                        [
                            72.0,
                            212.5
                        ],
                        [
                            532.5,
                            212.5
                        ],
                        [
                            532.5,
                            186.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 11,
                "parent_id": "34472c1c0daadade232ef7d1e2825394"
            },
            "text": "Seeking position in Information Systems or related field utilizing solid academic background along with exceptionally strong analytical, problem solving and customer service skills.",
            "type": "NarrativeText"
        },
        {
            "element_id": "0c18846f1793d97bdaaab2ccc32593f6",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            269.3,
                            234.3
                        ],
                        [
                            269.3,
                            246.3
                        ],
                        [
                            345.7,
                            246.3
                        ],
                        [
                            345.7,
                            234.3
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 11,
                "parent_id": "868242aff5ab9e45675f6ad08748e4e9"
            },
            "text": "EDUCATION",
            "type": "Title"
        },
        {
            "element_id": "7380977b1f183b5677296ee31ee7c165",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            254.1
                        ],
                        [
                            72.0,
                            279.7
                        ],
                        [
                            401.5,
                            279.7
                        ],
                        [
                            401.5,
                            254.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 11,
                "parent_id": "868242aff5ab9e45675f6ad08748e4e9"
            },
            "text": "BS in Computer Information Systems\u2014Web-based Networking Bellevue University, Bellevue NE",
            "type": "Title"
        },
        {
            "element_id": "46c7b40d900b94a7349022c6a6a39f8b",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            324.1,
                            267.7
                        ],
                        [
                            324.1,
                            293.5
                        ],
                        [
                            525.0,
                            293.5
                        ],
                        [
                            525.0,
                            267.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 11,
                "parent_id": "868242aff5ab9e45675f6ad08748e4e9"
            },
            "text": "Expected Graduation Date: January 20xx GPA to date: 3.86/4.00",
            "type": "Title"
        },
        {
            "element_id": "99af5fc2ab23627db09e19b9540d0f2c",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            281.5
                        ],
                        [
                            108.0,
                            293.5
                        ],
                        [
                            184.7,
                            293.5
                        ],
                        [
                            184.7,
                            281.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 11,
                "parent_id": "868242aff5ab9e45675f6ad08748e4e9"
            },
            "text": "Dean\u2019s Scholar",
            "type": "Title"
        },
        {
            "element_id": "0b08cd67d2d185256c2bbf3b02cd8c95",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            295.3
                        ],
                        [
                            72.0,
                            307.3
                        ],
                        [
                            484.7,
                            307.3
                        ],
                        [
                            484.7,
                            295.3
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 11,
                "parent_id": "868242aff5ab9e45675f6ad08748e4e9"
            },
            "text": "Associate of Applied Science, Metropolitan Community College, Omaha NE (20xx)",
            "type": "Title"
        },
        {
            "element_id": "8ea67b53409c20e8b84b0d4c59ff6199",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            309.1
                        ],
                        [
                            108.0,
                            321.1
                        ],
                        [
                            312.6,
                            321.1
                        ],
                        [
                            312.6,
                            309.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 11,
                "parent_id": "868242aff5ab9e45675f6ad08748e4e9"
            },
            "text": "Major: Management Information Systems",
            "type": "Title"
        },
        {
            "element_id": "ba347e6b2699d768337f80eb881883d0",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            396.1,
                            309.1
                        ],
                        [
                            396.1,
                            321.1
                        ],
                        [
                            474.8,
                            321.1
                        ],
                        [
                            474.8,
                            309.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 11,
                "parent_id": "8ea67b53409c20e8b84b0d4c59ff6199"
            },
            "text": "GPA: 3.45/4.00",
            "type": "UncategorizedText"
        },
        {
            "element_id": "d5f26d368085717c12b57862fa3e7876",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            189.7,
                            343.1
                        ],
                        [
                            189.7,
                            355.1
                        ],
                        [
                            425.2,
                            355.1
                        ],
                        [
                            425.2,
                            343.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 11,
                "parent_id": "868242aff5ab9e45675f6ad08748e4e9"
            },
            "text": "TECHNICAL KNOWLEDGE AND SKILLS",
            "type": "Title"
        },
        {
            "element_id": "ddeed308944eeee8978a3fe98c22e207",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            362.6
                        ],
                        [
                            72.0,
                            429.8
                        ],
                        [
                            521.0,
                            429.8
                        ],
                        [
                            521.0,
                            362.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 11,
                "parent_id": "d5f26d368085717c12b57862fa3e7876"
            },
            "text": "Operating Systems: Windows 19xx/20xx/XP/NT, UNIX/Linux Technical Support: Installation, Configuration & Troubleshooting of Hardware & Software Languages: Visual Basic, C, C++, Visual C++, Java, HTML, XML, ASP.NET Database Management: Relational Databases. SQL, PL/SQL, MS Access Applications: MS Office (Word, Excel, PowerPoint, Outlook), MS Project",
            "type": "NarrativeText"
        },
        {
            "element_id": "e344d8dab57cdb8f9ba1e41c91466707",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            218.4,
                            451.8
                        ],
                        [
                            218.4,
                            463.8
                        ],
                        [
                            396.6,
                            463.8
                        ],
                        [
                            396.6,
                            451.8
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 11,
                "parent_id": "868242aff5ab9e45675f6ad08748e4e9"
            },
            "text": "PROFESSIONAL EXPERIENCE",
            "type": "Title"
        },
        {
            "element_id": "e77464826ad21e0759773f35a3b3de81",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            471.4
                        ],
                        [
                            72.0,
                            556.8
                        ],
                        [
                            525.7,
                            556.8
                        ],
                        [
                            525.7,
                            471.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 11,
                "parent_id": "e344d8dab57cdb8f9ba1e41c91466707"
            },
            "text": "Computer Support Technician/Intern, Union Pacific Railroad, Omaha NE (Summer 20xx) \uf0b7 Assisted in systems administration and configuration in UNIX and Windows NT. \uf0b7 Installed and maintained local area networks, including Novell and Windows systems. \uf0b7 Staffed Help Desk; analyzed and resolved system problems encountered by end users. \uf0b7 Participated in the design and development of the department\u2019s web site. \uf0b7 Assisted with the maintenance of e-mail and other Internet applications.",
            "type": "NarrativeText"
        },
        {
            "element_id": "edfde95f008d7c0e9e8123031cf250b1",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            561.5
                        ],
                        [
                            72.0,
                            573.5
                        ],
                        [
                            442.0,
                            573.5
                        ],
                        [
                            442.0,
                            561.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 11,
                "parent_id": "868242aff5ab9e45675f6ad08748e4e9"
            },
            "text": "Computer Lab Assistant, Bellevue University, Bellevue NE (20xx \u2013 20xx)",
            "type": "Title"
        },
        {
            "element_id": "92f2e96890316543b9de62a6f577f51c",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            576.2
                        ],
                        [
                            90.0,
                            601.9
                        ],
                        [
                            538.2,
                            601.9
                        ],
                        [
                            538.2,
                            576.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 11,
                "parent_id": "edfde95f008d7c0e9e8123031cf250b1"
            },
            "text": "Provided advice and guidance to college students on the effective use of PCs and various software applications.",
            "type": "ListItem"
        },
        {
            "element_id": "aed2515c782d0ea6b9c0a69138d7664a",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            228.8,
                            623.9
                        ],
                        [
                            228.8,
                            635.9
                        ],
                        [
                            386.2,
                            635.9
                        ],
                        [
                            386.2,
                            623.9
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 11,
                "parent_id": "868242aff5ab9e45675f6ad08748e4e9"
            },
            "text": "COLLEGIATE ACTIVITIES",
            "type": "Title"
        },
        {
            "element_id": "828a8af9815658bad36ff2cdf28fc26e",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            643.5
                        ],
                        [
                            72.0,
                            669.3
                        ],
                        [
                            422.0,
                            669.3
                        ],
                        [
                            422.0,
                            643.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 11,
                "parent_id": "aed2515c782d0ea6b9c0a69138d7664a"
            },
            "text": "Volunteer Contributor, Bellevue University Computer Lab Newsletter Member, Varsity Baseball Team, Bellevue University",
            "type": "UncategorizedText"
        },
        {
            "element_id": "83c65b0c6c6c3462698333c496dda2f6",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            179.8,
                            697.2
                        ],
                        [
                            179.8,
                            709.2
                        ],
                        [
                            435.3,
                            709.2
                        ],
                        [
                            435.3,
                            697.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 11,
                "parent_id": "868242aff5ab9e45675f6ad08748e4e9"
            },
            "text": "REFERENCES AVAILABLE UPON REQUEST",
            "type": "Title"
        },
        {
            "element_id": "b89f4b2ac2e51c8784a1ddb399079165",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            446.0,
                            38.0
                        ],
                        [
                            446.0,
                            52.0
                        ],
                        [
                            543.6,
                            52.0
                        ],
                        [
                            543.6,
                            38.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 12
            },
            "text": "FUNCTIONAL",
            "type": "Header"
        },
        {
            "element_id": "cfb3b62b8b45c981025af3a93b3c1dfd",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            421.1,
                            67.0
                        ],
                        [
                            421.1,
                            135.9
                        ],
                        [
                            543.6,
                            135.9
                        ],
                        [
                            543.6,
                            67.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 12,
                "parent_id": "b89f4b2ac2e51c8784a1ddb399079165"
            },
            "text": "IM A. SAMPLE IX 987 Northridge Drive Omaha, Nebraska 68123 (402) 543-1234 imasample9@xxx.com",
            "type": "UncategorizedText"
        },
        {
            "element_id": "9628d4d77796a0bbf2a53610ec9316b3",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            152.9
                        ],
                        [
                            72.0,
                            179.7
                        ],
                        [
                            532.2,
                            179.7
                        ],
                        [
                            532.2,
                            152.9
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 12,
                "parent_id": "b89f4b2ac2e51c8784a1ddb399079165"
            },
            "text": "OBJECTIVE: Position in Human Resources Administration utilizing strong human relations, customer service and problem solving skills.",
            "type": "NarrativeText"
        },
        {
            "element_id": "415a187e76ca2bb8e2171d75cdc83325",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            198.2
                        ],
                        [
                            72.0,
                            211.1
                        ],
                        [
                            372.3,
                            211.1
                        ],
                        [
                            372.3,
                            198.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 12,
                "parent_id": "b89f4b2ac2e51c8784a1ddb399079165"
            },
            "text": "PROFESSIONAL SKILLS AND ACCOMPLISHMENTS",
            "type": "Title"
        },
        {
            "element_id": "8cd4a69ab2cf2a58f9a679fe3f865470",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            222.0
                        ],
                        [
                            90.0,
                            234.0
                        ],
                        [
                            246.8,
                            234.0
                        ],
                        [
                            246.8,
                            222.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 12,
                "parent_id": "b89f4b2ac2e51c8784a1ddb399079165"
            },
            "text": "Analysis and Problem Solving",
            "type": "Title"
        },
        {
            "element_id": "1dc4ce75c21b10e73958e9dc1e6350c7",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            235.5
                        ],
                        [
                            108.0,
                            275.2
                        ],
                        [
                            524.4,
                            275.2
                        ],
                        [
                            524.4,
                            235.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 12,
                "parent_id": "8cd4a69ab2cf2a58f9a679fe3f865470"
            },
            "text": "Researched and developed a survey instrument, subsequently used to obtain employee information on their satisfaction with the company\u2019s employee relations program.",
            "type": "ListItem"
        },
        {
            "element_id": "68e3c8a3b24f68d0c94153fd03c470c7",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            277.0
                        ],
                        [
                            108.0,
                            302.8
                        ],
                        [
                            498.5,
                            302.8
                        ],
                        [
                            498.5,
                            277.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 12,
                "parent_id": "8cd4a69ab2cf2a58f9a679fe3f865470"
            },
            "text": "Compiled and analyzed statistical data to identify potential sources for use in developing annual recruiting program.",
            "type": "ListItem"
        },
        {
            "element_id": "c6352a3d5e4a6a38a50601512c5c64c6",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            304.6
                        ],
                        [
                            108.0,
                            330.4
                        ],
                        [
                            525.4,
                            330.4
                        ],
                        [
                            525.4,
                            304.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 12,
                "parent_id": "8cd4a69ab2cf2a58f9a679fe3f865470"
            },
            "text": "Completed independent research project on the impact of \u201cfamily friendly\u201d human resources policies on employee retention.",
            "type": "ListItem"
        },
        {
            "element_id": "531f9bcc2519acf46ba0da83709bdc8e",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            332.2
                        ],
                        [
                            108.0,
                            358.0
                        ],
                        [
                            540.0,
                            358.0
                        ],
                        [
                            540.0,
                            332.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 12,
                "parent_id": "8cd4a69ab2cf2a58f9a679fe3f865470"
            },
            "text": "Conducted quality control inspections, analyzed results and developed action plans to address areas of concern.",
            "type": "ListItem"
        },
        {
            "element_id": "2e7d02073f80655af22354e4944e2816",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            363.0
                        ],
                        [
                            90.0,
                            375.0
                        ],
                        [
                            307.4,
                            375.0
                        ],
                        [
                            307.4,
                            363.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 12,
                "parent_id": "b89f4b2ac2e51c8784a1ddb399079165"
            },
            "text": "Communications and Customer Relations",
            "type": "Title"
        },
        {
            "element_id": "30b38c3a4226a66f1bf5cb9e155f01d2",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            376.6
                        ],
                        [
                            108.0,
                            402.4
                        ],
                        [
                            542.0,
                            402.4
                        ],
                        [
                            542.0,
                            376.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 12,
                "parent_id": "2e7d02073f80655af22354e4944e2816"
            },
            "text": "Provided orientation and training to new employees and advised them on the effective handling of customer complaints.",
            "type": "ListItem"
        },
        {
            "element_id": "de8e2eb729771f794b2c7ed79b1c362c",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            404.2
                        ],
                        [
                            108.0,
                            430.0
                        ],
                        [
                            484.5,
                            430.0
                        ],
                        [
                            484.5,
                            404.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 12,
                "parent_id": "2e7d02073f80655af22354e4944e2816"
            },
            "text": "Greeted applicants, scheduled interviews, conducted reference checks and participated in on-campus recruiting activities and career fairs.",
            "type": "ListItem"
        },
        {
            "element_id": "2e182f1563fbca098250eca7ae5a78bc",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            431.8
                        ],
                        [
                            108.0,
                            457.6
                        ],
                        [
                            535.5,
                            457.6
                        ],
                        [
                            535.5,
                            431.8
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 12,
                "parent_id": "2e7d02073f80655af22354e4944e2816"
            },
            "text": "Received Customer Service Satisfaction Award for high quality of services provided to both vendors and customers.",
            "type": "ListItem"
        },
        {
            "element_id": "4f0b12f2e261991e24c0e2d0b93ce44f",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            459.4
                        ],
                        [
                            108.0,
                            485.2
                        ],
                        [
                            524.5,
                            485.2
                        ],
                        [
                            524.5,
                            459.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 12,
                "parent_id": "2e7d02073f80655af22354e4944e2816"
            },
            "text": "Handled customer inquiries and sales; effectively represented company to vendors and prospective customers, resulting in a 15% increase in just six months.",
            "type": "ListItem"
        },
        {
            "element_id": "4c82ba7d6e9b99e89e7f5a4fdf626797",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            498.6
                        ],
                        [
                            72.0,
                            510.6
                        ],
                        [
                            148.3,
                            510.6
                        ],
                        [
                            148.3,
                            498.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 12,
                "parent_id": "b89f4b2ac2e51c8784a1ddb399079165"
            },
            "text": "EDUCATION",
            "type": "Title"
        },
        {
            "element_id": "4db1d7d00fa334c6f0d1d4b763cf6b9c",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            521.4
                        ],
                        [
                            90.0,
                            533.4
                        ],
                        [
                            431.4,
                            533.4
                        ],
                        [
                            431.4,
                            521.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 12,
                "parent_id": "b89f4b2ac2e51c8784a1ddb399079165"
            },
            "text": "Bachelor of Science, Bellevue University, Bellevue, NE (In Progress)",
            "type": "Title"
        },
        {
            "element_id": "8da362d2160f9e40a52fe7f709098a83",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            536.1
                        ],
                        [
                            108.0,
                            577.5
                        ],
                        [
                            298.7,
                            577.5
                        ],
                        [
                            298.7,
                            536.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 12,
                "parent_id": "4db1d7d00fa334c6f0d1d4b763cf6b9c"
            },
            "text": "Major: Psychology \uf0b7 Expected Graduation: August 20xx \uf0b7 GPA to date: 3.98/4.00",
            "type": "ListItem"
        },
        {
            "element_id": "3e0185b94d2edc39e3b91c938fbd9d11",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            360.1,
                            536.2
                        ],
                        [
                            360.1,
                            548.2
                        ],
                        [
                            500.4,
                            548.2
                        ],
                        [
                            500.4,
                            536.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 12,
                "parent_id": "b89f4b2ac2e51c8784a1ddb399079165"
            },
            "text": "Minor: Communication Arts",
            "type": "Title"
        },
        {
            "element_id": "2930e8b6b2bdcddef3f375af008ddc26",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            360.1,
                            565.5
                        ],
                        [
                            360.1,
                            577.5
                        ],
                        [
                            436.8,
                            577.5
                        ],
                        [
                            436.8,
                            565.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 12,
                "parent_id": "b89f4b2ac2e51c8784a1ddb399079165"
            },
            "text": "Dean\u2019s Scholar",
            "type": "Title"
        },
        {
            "element_id": "f0ce8210812214538dd5108bf83caf6d",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            582.1
                        ],
                        [
                            90.0,
                            594.1
                        ],
                        [
                            484.1,
                            594.1
                        ],
                        [
                            484.1,
                            582.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 12,
                "parent_id": "b89f4b2ac2e51c8784a1ddb399079165"
            },
            "text": "Associate of Arts, Iowa Western Community College, Council Bluffs, IA (20xx)",
            "type": "Title"
        },
        {
            "element_id": "93c21030309f099c936a54d4bc6a34ec",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            596.8
                        ],
                        [
                            108.0,
                            608.9
                        ],
                        [
                            339.8,
                            608.9
                        ],
                        [
                            339.8,
                            596.8
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 12,
                "parent_id": "f0ce8210812214538dd5108bf83caf6d"
            },
            "text": "Area of Emphasis: Business Administration",
            "type": "ListItem"
        },
        {
            "element_id": "1a28596e63f6f0434291cfb6cd3b863e",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            621.6
                        ],
                        [
                            72.0,
                            634.6
                        ],
                        [
                            196.3,
                            634.6
                        ],
                        [
                            196.3,
                            621.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 12,
                "parent_id": "b89f4b2ac2e51c8784a1ddb399079165"
            },
            "text": "WORK EXPERIENCE",
            "type": "Title"
        },
        {
            "element_id": "29a632d2f1c6b594a59e6c9a82388df2",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            645.2
                        ],
                        [
                            90.0,
                            674.0
                        ],
                        [
                            488.3,
                            674.0
                        ],
                        [
                            488.3,
                            645.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 12,
                "parent_id": "1a28596e63f6f0434291cfb6cd3b863e"
            },
            "text": "Senior Sales Associate, Precision Tool, Omaha, NE (20xx to present) Human Resources Intern, Oriental Trading, Omaha, NE (Spring Semester 20xx)",
            "type": "UncategorizedText"
        },
        {
            "element_id": "d4190bbcb05f009516af82a4ef55b41a",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            687.5
                        ],
                        [
                            72.0,
                            699.5
                        ],
                        [
                            326.8,
                            699.5
                        ],
                        [
                            326.8,
                            687.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 12,
                "parent_id": "b89f4b2ac2e51c8784a1ddb399079165"
            },
            "text": "REFERENCES FURNISHED UPON REQUEST",
            "type": "Title"
        },
        {
            "element_id": "c9d68a66c89acda542a844178f45a531",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            220.4,
                            38.0
                        ],
                        [
                            220.4,
                            52.0
                        ],
                        [
                            543.6,
                            52.0
                        ],
                        [
                            543.6,
                            38.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13
            },
            "text": "CHRONOLOGICAL (HUMAN/SOCIAL SERVICE)",
            "type": "Header"
        },
        {
            "element_id": "3ba57b763de5fa478318a3b22c85ae6d",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            250.4,
                            66.8
                        ],
                        [
                            250.4,
                            80.8
                        ],
                        [
                            365.1,
                            80.8
                        ],
                        [
                            365.1,
                            66.8
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "c9d68a66c89acda542a844178f45a531"
            },
            "text": "IM A. SAMPLE X",
            "type": "Title"
        },
        {
            "element_id": "563358a214bd68d4b053ab46680c3ffc",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            82.2
                        ],
                        [
                            72.0,
                            106.0
                        ],
                        [
                            226.7,
                            106.0
                        ],
                        [
                            226.7,
                            82.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "3ba57b763de5fa478318a3b22c85ae6d"
            },
            "text": "3083 North South Street, Apt. A-1 Grand Island, Nebraska 68803",
            "type": "NarrativeText"
        },
        {
            "element_id": "9af6ac3828f29e67571d5fac44d1d424",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            432.1,
                            82.2
                        ],
                        [
                            432.1,
                            106.0
                        ],
                        [
                            541.8,
                            106.0
                        ],
                        [
                            541.8,
                            82.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "3ba57b763de5fa478318a3b22c85ae6d"
            },
            "text": "(308) 308-3083 imasample10@xxxx.net",
            "type": "UncategorizedText"
        },
        {
            "element_id": "8d3f63595e295748cf913d0571593fb1",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            271.4,
                            126.5
                        ],
                        [
                            271.4,
                            138.5
                        ],
                        [
                            351.8,
                            138.5
                        ],
                        [
                            351.8,
                            126.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "3ba57b763de5fa478318a3b22c85ae6d"
            },
            "text": "OBJECTIVE\uf020",
            "type": "UncategorizedText"
        },
        {
            "element_id": "50455fea1bff6ce5fe39f54983cf4433",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            145.8
                        ],
                        [
                            72.0,
                            169.6
                        ],
                        [
                            531.5,
                            169.6
                        ],
                        [
                            531.5,
                            145.8
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "3ba57b763de5fa478318a3b22c85ae6d"
            },
            "text": "Seeking Position in Human/Social Service Administration or related field utilizing strong academic background, experience and excellent interpersonal skills",
            "type": "NarrativeText"
        },
        {
            "element_id": "6e5068034a978e5cdd449161ec394513",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            269.3,
                            180.7
                        ],
                        [
                            269.3,
                            192.7
                        ],
                        [
                            345.7,
                            192.7
                        ],
                        [
                            345.7,
                            180.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "c9d68a66c89acda542a844178f45a531"
            },
            "text": "EDUCATION",
            "type": "Title"
        },
        {
            "element_id": "bbadcce68bb7248b80ca50be5868cc48",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            200.2
                        ],
                        [
                            72.0,
                            223.8
                        ],
                        [
                            504.2,
                            223.8
                        ],
                        [
                            504.2,
                            200.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "6e5068034a978e5cdd449161ec394513"
            },
            "text": "BS in Human & Social Service Administration, Bellevue University, Bellevue, NE (Jan 20xx) GPA: 3.81/4.00",
            "type": "UncategorizedText"
        },
        {
            "element_id": "028a0858af4137a7d7c607ace8490267",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            212.6
                        ],
                        [
                            90.0,
                            223.8
                        ],
                        [
                            178.3,
                            223.8
                        ],
                        [
                            178.3,
                            212.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "c9d68a66c89acda542a844178f45a531"
            },
            "text": "\uf0a7 Dean\u2019s Scholar",
            "type": "Title"
        },
        {
            "element_id": "a7fd093cbcede8ced847728b2953e1d8",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            228.4
                        ],
                        [
                            72.0,
                            239.4
                        ],
                        [
                            482.6,
                            239.4
                        ],
                        [
                            482.6,
                            228.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "028a0858af4137a7d7c607ace8490267"
            },
            "text": "AAS in Human Services (Dec 19xx), 75-Hr Basic Nursing Assistant Program (Jan 20xx)",
            "type": "UncategorizedText"
        },
        {
            "element_id": "e1e6f78ecffd5c39365e042525d800f9",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            241.1
                        ],
                        [
                            90.0,
                            252.1
                        ],
                        [
                            369.9,
                            252.1
                        ],
                        [
                            369.9,
                            241.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "c9d68a66c89acda542a844178f45a531"
            },
            "text": "Central Community College\u2014Hastings Campus, Hastings, NE",
            "type": "Title"
        },
        {
            "element_id": "2de1488d54075f61e55e0fce35c67e29",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            257.2,
                            263.3
                        ],
                        [
                            257.2,
                            275.3
                        ],
                        [
                            357.9,
                            275.3
                        ],
                        [
                            357.9,
                            263.3
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "c9d68a66c89acda542a844178f45a531"
            },
            "text": "WORK HISTORY",
            "type": "Title"
        },
        {
            "element_id": "5033603eb5f28525ebab6b944fa47138",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            282.8
                        ],
                        [
                            72.0,
                            357.0
                        ],
                        [
                            538.8,
                            357.0
                        ],
                        [
                            538.8,
                            282.8
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "2de1488d54075f61e55e0fce35c67e29"
            },
            "text": "Day Rehabilitation Specialist, Greater NE Goodwill Industries, Grand Island, NE (June 20xx \u2013 Present) \uf0a7 Manage a caseload of twenty consumers, assist them in setting and reaching individual plans \uf0a7 Facilitate group sessions on Mental Illness, Stress Management and Healthy Relationships \uf0a7 Plan and implement social activities for consumers \uf0a7 Coordinate and conduct team meetings \uf0a7 Process billings, manage petty cash fund, and oversee operations in supervisor\u2019s absence",
            "type": "NarrativeText"
        },
        {
            "element_id": "c6f3ab33b1a95b89cf54dbfc564fd9c9",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            361.6
                        ],
                        [
                            72.0,
                            372.6
                        ],
                        [
                            469.3,
                            372.6
                        ],
                        [
                            469.3,
                            361.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "2de1488d54075f61e55e0fce35c67e29"
            },
            "text": "Assistant Receptionist, Tiffany Square Care Center, Grand Island, NE (Jan \u2013 June 20xx)",
            "type": "UncategorizedText"
        },
        {
            "element_id": "bdbb4b01179ad429528b162e9942e296",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            374.2
                        ],
                        [
                            90.0,
                            423.3
                        ],
                        [
                            518.6,
                            423.3
                        ],
                        [
                            518.6,
                            374.2
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "2de1488d54075f61e55e0fce35c67e29"
            },
            "text": "\uf0a7 Arranged and facilitated weekend activities for residents \uf0a7 Contacted families to set up dates and times to review and discuss care plans \uf0a7 Delivered and read mail to residents, providing companionship and social interaction \uf0a7 Filed confidential paperwork and provided receptionist/administrative support for the Center",
            "type": "NarrativeText"
        },
        {
            "element_id": "edec2414c9f24552469cdb0dec7b5767",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            427.8
                        ],
                        [
                            72.0,
                            438.9
                        ],
                        [
                            513.0,
                            438.9
                        ],
                        [
                            513.0,
                            427.8
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "2de1488d54075f61e55e0fce35c67e29"
            },
            "text": "Employment Trainer, Central NE Goodwill Industries, Grand Island, NE (Aug 19xx \u2013 May 20xx)",
            "type": "UncategorizedText"
        },
        {
            "element_id": "40c856bf87c59218df7eb4ebecb47046",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            440.5
                        ],
                        [
                            90.0,
                            464.2
                        ],
                        [
                            541.3,
                            464.2
                        ],
                        [
                            541.3,
                            440.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "2de1488d54075f61e55e0fce35c67e29"
            },
            "text": "\uf0a7 Managed a caseload of twenty consumers and provided on-the-job coaching to help them succeed \uf0a7 Conducted group job search training sessions and assisted consumers with completion of job",
            "type": "NarrativeText"
        },
        {
            "element_id": "5bd73f7a6d78001bcd24e0d73e0b75cf",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            465.9
                        ],
                        [
                            108.0,
                            476.9
                        ],
                        [
                            283.7,
                            476.9
                        ],
                        [
                            283.7,
                            465.9
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "c9d68a66c89acda542a844178f45a531"
            },
            "text": "applications, cover letters and resumes",
            "type": "Title"
        },
        {
            "element_id": "fb6e7c308abf5f0137fedc69f0961ac2",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            481.5
                        ],
                        [
                            72.0,
                            505.1
                        ],
                        [
                            530.5,
                            505.1
                        ],
                        [
                            530.5,
                            481.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "5bd73f7a6d78001bcd24e0d73e0b75cf"
            },
            "text": "Criminal Justice/Shelter Advocate, Crisis Center Inc & Family Violence Coalition, Grand Island, NE (July 20xx \u2013 Oct 20xx)",
            "type": "UncategorizedText"
        },
        {
            "element_id": "bce748623d0ea960f478f544af36d7ff",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            506.7
                        ],
                        [
                            90.0,
                            530.5
                        ],
                        [
                            533.6,
                            530.5
                        ],
                        [
                            533.6,
                            506.7
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "5bd73f7a6d78001bcd24e0d73e0b75cf"
            },
            "text": "\uf0a7 Responded to crisis calls and provided support to victims of domestic abuse \uf0a7 Completed paperwork to document circumstances surrounding alleged abuse for judicial review",
            "type": "NarrativeText"
        },
        {
            "element_id": "dd319c8de0d4b3c523cc44a502378dc1",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            535.1
                        ],
                        [
                            72.0,
                            546.2
                        ],
                        [
                            504.7,
                            546.2
                        ],
                        [
                            504.7,
                            535.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "5bd73f7a6d78001bcd24e0d73e0b75cf"
            },
            "text": "Social Services Assistant, Tiffany Square Care Center, Grand Island, NE (Jan 20xx \u2013 Sept 20xx)",
            "type": "UncategorizedText"
        },
        {
            "element_id": "d3ad5a7c40bb760322c3eb98d33073be",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            547.6
                        ],
                        [
                            90.0,
                            571.4
                        ],
                        [
                            537.2,
                            571.4
                        ],
                        [
                            537.2,
                            547.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "5bd73f7a6d78001bcd24e0d73e0b75cf"
            },
            "text": "\uf0a7 Conducted tours, provided orientation and general assistance for new residents \uf0a7 Completed social histories, inventoried clothing, and met one-on-one with residents to help them",
            "type": "NarrativeText"
        },
        {
            "element_id": "81fa733c6e1f703457c8240e6dcd62ab",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            573.1
                        ],
                        [
                            108.0,
                            584.1
                        ],
                        [
                            297.8,
                            584.1
                        ],
                        [
                            297.8,
                            573.1
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "5bd73f7a6d78001bcd24e0d73e0b75cf"
            },
            "text": "understand their rights and responsibilities",
            "type": "NarrativeText"
        },
        {
            "element_id": "48582ca711fd591ddc4e8e236ad29bdc",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            585.5
                        ],
                        [
                            90.0,
                            596.7
                        ],
                        [
                            537.0,
                            596.7
                        ],
                        [
                            537.0,
                            585.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "5bd73f7a6d78001bcd24e0d73e0b75cf"
            },
            "text": "\uf0a7 Assisted the Center in meeting critical staffing needs during peak times by working as a certified",
            "type": "NarrativeText"
        },
        {
            "element_id": "e7599c0a8ce408fc4cddead2a927b4e1",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            598.4
                        ],
                        [
                            108.0,
                            609.4
                        ],
                        [
                            364.0,
                            609.4
                        ],
                        [
                            364.0,
                            598.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "c9d68a66c89acda542a844178f45a531"
            },
            "text": "nursing assistant, dietary aide, receptionist and van driver",
            "type": "Title"
        },
        {
            "element_id": "0b7a7281922686b6bf1cf5a8c529c269",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            238.1,
                            620.6
                        ],
                        [
                            238.1,
                            632.6
                        ],
                        [
                            376.9,
                            632.6
                        ],
                        [
                            376.9,
                            620.6
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "c9d68a66c89acda542a844178f45a531"
            },
            "text": "COMMUNITY SERVICE",
            "type": "Title"
        },
        {
            "element_id": "d32e9a9f93a36ff6384d4a8e006af401",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            72.0,
                            640.0
                        ],
                        [
                            72.0,
                            651.1
                        ],
                        [
                            419.7,
                            651.1
                        ],
                        [
                            419.7,
                            640.0
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "c9d68a66c89acda542a844178f45a531"
            },
            "text": "Volunteer, Women\u2019s Health Services, Grand Island, NE (Fall 20xx \u2013 present)",
            "type": "Title"
        },
        {
            "element_id": "5c1e7896d6630ea743bff563b4366e44",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            652.5
                        ],
                        [
                            90.0,
                            663.7
                        ],
                        [
                            542.5,
                            663.7
                        ],
                        [
                            542.5,
                            652.5
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "d32e9a9f93a36ff6384d4a8e006af401"
            },
            "text": "\uf0a7 Assisted professional staff and participated in one-on-one discussions with women seeking advice",
            "type": "NarrativeText"
        },
        {
            "element_id": "b29c6d86c7136e178d67a754314708c3",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            108.0,
                            665.4
                        ],
                        [
                            108.0,
                            676.4
                        ],
                        [
                            214.0,
                            676.4
                        ],
                        [
                            214.0,
                            665.4
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "c9d68a66c89acda542a844178f45a531"
            },
            "text": "on health-related issues",
            "type": "Title"
        },
        {
            "element_id": "070e1b6e9b60add7dde98988c8251f31",
            "metadata": {
                "coordinates": {
                    "layout_height": 792.0,
                    "layout_width": 612.0,
                    "points": [
                        [
                            90.0,
                            677.8
                        ],
                        [
                            90.0,
                            689.0
                        ],
                        [
                            523.9,
                            689.0
                        ],
                        [
                            523.9,
                            677.8
                        ]
                    ],
                    "system": "PixelSpace"
                },
                "file_directory": "./assets/files",
                "filename": "resume-sample.pdf",
                "filetype": "application/pdf",
                "languages": [
                    "eng"
                ],
                "last_modified": "2025-12-22T16:32:22",
                "page_number": 13,
                "parent_id": "b29c6d86c7136e178d67a754314708c3"
            },
            "text": "\uf0a7 Observed group training sessions to develop the skills needed to facilitate groups in the future",
            "type": "NarrativeText"
        }
    ]
    2.287718125000538
