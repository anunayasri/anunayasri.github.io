#!/usr/bin/python
from datetime import datetime
from pathlib import Path
import frontmatter

non_url_safe = ['"', '#', '$', '%', '&', '+', ',', '/', ':', ';', '=', '?',
                '@', '[', '\\', ']', '^', '`', '{', '|', '}', '~', "'"]

def slugify(text):
    non_safe = [c for c in text if c in non_url_safe]
    if non_safe:
        for c in non_safe:
            text = text.replace(c, '')
    # Strip leading, trailing and multiple whitespace, convert remaining whitespace to -
    text = u'-'.join(text.split())
    return text

def new_post():
    title = input("Title: ")
    if not title:
        raise ValueError('Title is mandatory.')

    date = datetime.today()
    slug = slugify(title)

    # Try creating the file
    md_file_path = f"content/posts/{date.strftime('%Y-%m-%d')}---{slug}"
    Path(md_file_path).touch()

    category = input('Category: ')
    if not category:
        raise ValueError('Category is mandatory.')

    tags = input('Tags(comma separated): ').split(',')
    if not tags:
        raise ValueError(f'Tags are mandatory. Entered values "{tags}"')

    description = input('Description: ') or ''

    metadata = dict(
        title=title,
        date=date,
        template='post',
        draft=True,
        slug=slug,
        category=category,
        tags=tags,
        description=description,
    )
    post = frontmatter.Post(content='', **metadata)

    # Write the metadata in the file
    with open(md_file_path) as f:
        f.write(str(frontmatter.dumps(post)))

    print(f"Written to {md_file_path}")


if __name__ == '__main__':
    new_post()
