# Changelog

## Week 03:

- **15.01.2025** create project using `uv`, add git connection, automatically clean notebook outputs[^1] and start working on getting data on cities in Poland


# Footnotes:

[^1]: How to setup: 

```
uv add pre-commit nbstripout
nbstripout --install
```

It creates file `.gitattributes` which should contain:

```
*.ipynb filter=nbstripout
```