# Changelog

## Week 03:

- **15.01.2026** create project using `uv`, add git connection, [automatically clean notebook outputs](#automatically-clean-notebook-output) and start working on getting data on cities in Poland
- **16.01.2026** explore cities data, plan to merge `node` with `way` and `relation`
- **17.01.2026** extract city names, positon and population; planned next steps to add administrative division

## Week 04:

- **19.01.2026** change the name of the package, install current project as a package, add function to download and save Open Street Maps and prepeare scripts to download data
- **20.01.2026** add utils function to convert polygons and multipolygons into points, add cache directory (invisible), get McDonalds' data, get boundaries data
- **21.01.2026** get voivodeships data
- **22.01.2026** join city data with voivodeship data and start working on mcdonald data
- **23.01.2026** add missing cities to mcdonald data, start working on clustering
- **24.01.2026** clusted data to remove duplicates, decided that if there is two restaurants on the motorway (in both way) tret them as one, download motorways data


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