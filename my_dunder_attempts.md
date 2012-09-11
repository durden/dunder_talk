# My Dunder ideas/attempts

    !python

    >>> from frappy.services.github import Github
    >>> g = Github()
    >>> result = g.users('octocat')
    >>> result.response_json
    >>> # http://developer.github.com/v3/users/

    __getattr__(self, name)
    __call__(self, *args, **kwargs)

- <strike>Extra documentation</strike>
- <strike>Update for minor API changes</strike>
- Web API wrapper [frappy](http://github.com/durden/frappy)

# Presenter Notes

- Main idea was to have a python wrapper for any REST API that didn't need it's
  own documentation or constant updates.
- Metaprogramming
- Create object with base domain name to query
- Add missing attributes onto url, add args at the end as query string

--------------------------------------------------

# Better than a Frappy

## Hammock

    !python

    >>> from hammock import Hammock as Github

    >>> # Let's create the first chain of hammock using base api url
    >>> github = Github('https://api.github.com')

    >>> # Ok, let the magic happens, ask github for hammock watchers
    >>> resp = github.repos('kadirpekel', 'hammock').watchers.GET()

    __getattr__(self, name)
    __call__(self, *args, **kwargs)
    __iter__(self)
    __repr__(self)

- Chains 'hammock' objects
- Allows arguments anywhere
- [hammock](https://github.com/kadirpekel/hammock)
