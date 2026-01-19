# Changelog

## Week 03:

- **15.01.2026** create project using `uv`, add git connection, [automatically clean notebook outputs](#automatically-clean-notebook-output) and start working on getting data on cities in Poland
- **16.01.2026** explore cities data, plan to merge `node` with `way` and `relation`
- **17.01.2026** extract city names, positon and population; planned next steps to add administrative division

## Week 04:

- **19.01.2026** add utils function to convert polygons and multipolygons into points, add cache directory (invisible), get McDonalds' data, get boundaries data. 


# Footnotes:

## Automatically Clean Notebook Output

```
uv add pre-commit nbstripout
nbstripout --install
```

It creates file `.gitattributes` which should contain:

```
*.ipynb filter=nbstripout
```