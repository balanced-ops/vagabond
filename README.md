# Vagabond

At [Balanced](https://github.com/balanced), we use [Vagrant](https://github.com/mitchellh/vagrant) for all our developer work. These are common settings, helpers, and utilities for facilitating `Vagrantfile` management as well as other virtualization environments.

## Getting Started

Given that [Vagrant](https://github.com/mitchellh/vagrant)'s `Vagrantfile` is just plain ruby code, it is [possible](https://github.com/purpleidea/oh-my-vagrant/blob/master/vagrant/Vagrantfile) to extend it
in many different ways.

However, it is preferable that we try to enforce uniformity across the `Vagrantfile`, so custom ruby code for modifications is
discouraged. If there's an addition that is welcome to the project, please open up a github issue.

That being said, the current way to utilize `Vagabond` is to use it as submodule in a parent project.

## Vagabond as a `submodule` in a parent project

The current way on how to use `Vagabond` is to include it as a git submodule. Then run:

```bash
ln -s vagabond/Vagrantfile
```

There's an experimental `install.py` to setup this for you, but it's not done yet and I'm not sure if it's needed.

## Customizations

Most developers will have custom settings, i.e. locations on where code will be stored,
and they they will also need to customize the machine for their own machines or maybe
even using remote clouds.

Projects like the below can help produce this effect:
- https://github.com/maoueh/nugrant
- https://github.com/PraxisLabs/vagrant-pirate

### [Nugrant](https://github.com/maoueh/nugrant)

We are currently experimenting with [Nugrant](https://github.com/maoueh/nugrant). Here's an example
`.vagrantuser` file that you can include in the parent directory of where you've cloned this repository.

```yaml
# -*- mode: yaml -*-
---
providers: {
  virtualbox: {
    memory: 4096,
    cpus: 2
  },
  aws: {
    region: us-west-1,
    availability_zone: us-west-1a,
    ssh_key: ~/.ssh/id_rsa.pub,
    flavor_id: m3.2xlarge,
    iam_profile_name: some-profile,
  }
}

synced_folders:
  - folder_1
  - folder_2

exec:
  - "ENV['USER']"
```

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

## Why is this its own repo?

Borrowing from this [StackOverflow Question](http://superuser.com/questions/737416/should-a-vagrant-project-be-its-own-repo) and
this [Vagrant mailing-list question](https://groups.google.com/forum/#!topic/vagrant-up/jqLVh6CKBek), it seems that this is a
common concern.

[Balanced](https://github.com/balanced) has previously used one `Vagrantfile` per project and that didnt' scale as many
`Vagrantfile`s were divergent and required constant updating.

From this other stackoverflow question about [git repo in a subdirectory](http://stackoverflow.com/questions/22646795/how-to-properly-manage-a-git-repo-in-a-subdirectory-ignored-by-the-parent-direc/22736757#22736757), we can also see this is the general direction to take.

## Hacking on Vagabond

```bash
git clone git@github.com:balanced-cookbooks/vagabond.git
```

## Why the name Vagabond?

It was either that or hobo :-D
