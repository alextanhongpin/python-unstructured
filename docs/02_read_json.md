

``` python
from unstructured.staging.base import convert_to_dict, elements_from_json

elements = elements_from_json(filename="output.json")

elements = convert_to_dict(elements)
for element in elements[:5]:
    print(f"{element['type']}: {element['text']}")
```

    Title: RESUME SAMPLES
    NarrativeText: Preparing an effective resume is a difficult and time-consuming task. This handout
    NarrativeText: contains resume examples that will help you get started. Different formats and styles
    NarrativeText: are used to illustrate the various suggestions and tips contained in the handout,
    Title: "Preparing Your Resume," also available through the Bellevue University Career Services

``` python
from unstructured.cleaners.core import replace_unicode_quotes
```

``` python
for element in elements:
    if element["text"] != (clean := replace_unicode_quotes(element["text"])):
        print(clean)
```

``` python
import pandas as pd

df = pd.DataFrame(data=elements)
df = df[["type", "text"]]
df
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|     | type          | text                                              |
|-----|---------------|---------------------------------------------------|
| 0   | Title         | RESUME SAMPLES                                    |
| 1   | NarrativeText | Preparing an effective resume is a difficult a... |
| 2   | NarrativeText | contains resume examples that will help you ge... |
| 3   | NarrativeText | are used to illustrate the various suggestions... |
| 4   | Title         | "Preparing Your Resume," also available throug... |
| ... | ...           | ...                                               |
| 278 | Title         | COMMUNITY SERVICE                                 |
| 279 | Title         | Volunteer, Women’s Health Services, Grand Isla... |
| 280 | NarrativeText |  Assisted professional staff and participated... |
| 281 | Title         | on health-related issues                          |
| 282 | NarrativeText |  Observed group training sessions to develop ... |

<p>283 rows × 2 columns</p>
</div>

``` python
from functools import partial

from unstructured.cleaners.core import clean, clean_bullets, clean_non_ascii_chars

df["cleaned"] = df["text"].apply(
    partial(
        clean,
        bullets=True,
        dashes=True,
        extra_whitespace=True,
        trailing_punctuation=True,
    )
)
df["cleaned"] = df["cleaned"].apply(clean_non_ascii_chars)
df["cleaned"] = df["cleaned"].str.strip()
df["has_changed"] = df["cleaned"] == df["text"]
df.head()
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|  | type | text | cleaned | has_changed |
|----|----|----|----|----|
| 0 | Title | RESUME SAMPLES | RESUME SAMPLES | True |
| 1 | NarrativeText | Preparing an effective resume is a difficult a... | Preparing an effective resume is a difficult a... | False |
| 2 | NarrativeText | contains resume examples that will help you ge... | contains resume examples that will help you ge... | True |
| 3 | NarrativeText | are used to illustrate the various suggestions... | are used to illustrate the various suggestions... | False |
| 4 | Title | "Preparing Your Resume," also available throug... | "Preparing Your Resume," also available throug... | True |

</div>

``` python
# https://pandas.pydata.org/docs/user_guide/options.html
with pd.option_context("max_colwidth", 1, "display.expand_frame_repr", True):
    print("before:", df.shape)
    df_len = df[df["cleaned"].str.len() > 0]
    print("after:", df_len.shape)
    print()
    print(df_len["cleaned"].head())
```

    before: (283, 4)
    after: (281, 4)

    0    RESUME SAMPLES                                                                         
    1    Preparing an effective resume is a difficult and time consuming task. This handout     
    2    contains resume examples that will help you get started. Different formats and styles  
    3    are used to illustrate the various suggestions and tips contained in the handout       
    4    "Preparing Your Resume," also available through the Bellevue University Career Services
    Name: cleaned, dtype: object

``` python
from unstructured.staging.base import convert_to_dataframe

elements = elements_from_json(filename="output.json")

df = convert_to_dataframe(elements)
df.head()
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|  | type | element_id | text | coordinates_points | coordinates_system | coordinates_layout_width | coordinates_layout_height | file_directory | filename | filetype | languages | last_modified | page_number | parent_id | links |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| 0 | Title | a2a2f5e11ab0fa191c638aae9a20285a | RESUME SAMPLES | ((212.8, 163.0), (212.8, 183.1), (404.8, 183.1... | PixelSpace | 612.0 | 792.0 | ./assets/files | resume-sample.pdf | application/pdf | \[eng\] | 2025-12-22T16:32:22 | 1 | NaN | NaN |
| 1 | NarrativeText | cc23138894eb24a8caeba30d37b94807 | Preparing an effective resume is a difficult a... | ((72.0, 209.8), (72.0, 223.8), (509.9, 223.8),... | PixelSpace | 612.0 | 792.0 | ./assets/files | resume-sample.pdf | application/pdf | \[eng\] | 2025-12-22T16:32:22 | 1 | a2a2f5e11ab0fa191c638aae9a20285a | NaN |
| 2 | NarrativeText | 8c8fdcf2ebeda0f357c9434d45881f92 | contains resume examples that will help you ge... | ((72.0, 234.1), (72.0, 248.2), (524.9, 248.2),... | PixelSpace | 612.0 | 792.0 | ./assets/files | resume-sample.pdf | application/pdf | \[eng\] | 2025-12-22T16:32:22 | 1 | a2a2f5e11ab0fa191c638aae9a20285a | NaN |
| 3 | NarrativeText | 99baa9431110902f41be26a0902f57dd | are used to illustrate the various suggestions... | ((72.0, 258.5), (72.0, 272.6), (491.0, 272.6),... | PixelSpace | 612.0 | 792.0 | ./assets/files | resume-sample.pdf | application/pdf | \[eng\] | 2025-12-22T16:32:22 | 1 | a2a2f5e11ab0fa191c638aae9a20285a | NaN |
| 4 | Title | 8761e1b55d06b00175d5bd098022aafd | "Preparing Your Resume," also available throug... | ((72.0, 282.9), (72.0, 296.9), (535.8, 296.9),... | PixelSpace | 612.0 | 792.0 | ./assets/files | resume-sample.pdf | application/pdf | \[eng\] | 2025-12-22T16:32:22 | 1 | NaN | NaN |

</div>

``` python
from unstructured.chunking.title import chunk_by_title

chunks = chunk_by_title(elements)
for chunk in chunks[:5]:
    print(chunk)
    print("\n\n" + "-" * 80)
```

    RESUME SAMPLES

    Preparing an effective resume is a difficult and time-consuming task. This handout

    contains resume examples that will help you get started. Different formats and styles

    are used to illustrate the various suggestions and tips contained in the handout,

    "Preparing Your Resume," also available through the Bellevue University Career Services


    --------------------------------------------------------------------------------
    Center.

    Remember, these are intended to serve only as examples. You should modify or change

    as appropriate to customize your resume according to your skills, experience, education,

    and the job you’re applying.

    For additional guidance or assistance, contact the Career Services Center at

    (402) 557-7423, (800) 756-7920 ext. 7423 or careerservices@bellevue.edu.


    --------------------------------------------------------------------------------
    A Word of Caution: Please don’t be tempted to use one of the Resume Wizards or Templates that are available online or included in many word processing programs. They can be difficult to work with, don’t allow you to present yourself in the best possible light—and employers can identify them easily. Instead, create your resume as a simple document in MS Word, like the examples included in this handout.

    Revision: June 2015

    FUNCTIONAL (EXPERIENCED)


    --------------------------------------------------------------------------------
    IM A. SAMPLE I 1234 North 55 Street Bellevue, Nebraska 68005 (402) 292-2345 imasample1@xxx.com

    SUMMARY OF QUALIFICATIONS

    Exceptionally well organized and resourceful Professional with more than six years experience and a solid academic background in accounting and financial management; excellent analytical and problem solving skills; able to handle multiple projects while producing high quality work in a fast-paced, deadline-oriented environment.

    EDUCATION


    --------------------------------------------------------------------------------
    Bachelor of Science, Bellevue University, Bellevue, NE (In Progress)

    Major: Accounting Expected Graduation Date: January, 20xx

    Minor: Computer Information Systems GPA to date: 3.95/4.00


    --------------------------------------------------------------------------------
