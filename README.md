# Vagabond

At [Balanced](https://github.com/balanced), we use [Vagrant](https://github.com/mitchellh/vagrant) for all our developer work. These are common settings, helpers, and utilities for facilitating `Vagrantfile` management as well as other virtualization environments.

## Getting Started

Given that [Vagrant](https://github.com/mitchellh/vagrant)'s `Vagrantfile` is just plain ruby code, it is possible to extend it
in many different ways.

However, it is preferable that we try to enforce uniformity across the `Vagrantfile`, so custom ruby code for modifications is
discouraged. If there's an addition that is welcome to the project, please open up a github issue.

That being said, the current way to utilize `Vagabond` is to use it as submodule in a parent project.

## Vagabond as a `submodule` in a parent project

The current way on how to use `Vagabond` is to include it as a git submodule

### Updating Vagabond's submodule

[This trick is really cool to update git submodules](http://scribu.net/blog/git-alias-for-updating-submodules.html) and serves as a really neat way to manage and update git submodules.

First, run this:

```bash
git config --global alias.up-sub '!f() { cd $1 && git checkout master && git pull && git submodule update --init --recursive; }; f
```

Then, when you can easily update to the latest `Vagabond` by running:

```bash
git up-sub vagabond
```

## Customizations

Most developers will have custom settings, i.e. locations on where code will be stored,
and they they will also need to customize the machine for their own machines or maybe
even using remote clouds.

Projects like the below can help produce this effect:
- https://github.com/maoueh/nugrant
- https://github.com/PraxisLabs/vagrant-pirate

### Why is this its own repo?

Borrowing from this [StackOverflow Question](http://superuser.com/questions/737416/should-a-vagrant-project-be-its-own-repo) and
this [Vagrant mailing-list question](https://groups.google.com/forum/#!topic/vagrant-up/jqLVh6CKBek), it seems that this is a
common concern.

[Balanced](https://github.com/balanced) has previously used one `Vagrantfile` per project and that didnt' scale as many
`Vagrantfile`s were divergent and required constant updating.

## Hacking on Vagabond

```bash
git clone git@github.com:balanced-cookbooks/vagabond.git
```

## Why the name Vagabond?

It was either that or hobo :-D
