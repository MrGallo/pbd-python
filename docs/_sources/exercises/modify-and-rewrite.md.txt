# Modify and Rewrite


Download the JSON file.

```eval_rst
* :download:`exercises.json <examples/exercises.json>`
```

Create a program that will load the list of exercises, change some things listed below, then overwrite the file.

Make the following changes for every exercise in the list:
- Remove the `number` key
- Convert the `points` key to `int`
- Add a `published` key and set the value to `False`

The `exercises.json` is an actual subset of the `.json` file I use to help generate this website. Some of these operations I actually needed to perform at one point.

## What you should end up with

```
[
    {
        "section": "Dictionaries",
        "name": "Person Info",
        "points": 10,
        "published": false
    },
    {
        "section": "Dictionaries",
        "name": "Mini Passivist RPG",
        "points": 25,
        "published": false
    },
    .
    .
    .
]
```