Title: About
Slug: about

## Why Mocka exists

Mocka is a GTK desktop built for FreeBSD and GhostBSD first.

Most desktop environments are designed on Linux and ported to the BSDs
afterward. They work, but they carry assumptions that don't belong on a BSD
system, and those assumptions show up as missing features, workarounds, and
patches that downstream projects have to maintain. Mocka starts from the
other side: FreeBSD and GhostBSD are the target platforms, not a port.

## Why a reimplementation instead of a fork

The obvious path would have been to fork MATE and change it. We chose not to.

**A clean license.** Forked code keeps its original license. Every Mocka
component is new code, released under the BSD-3-Clause license, the same
family of license as FreeBSD and GhostBSD themselves.

**No inherited assumptions.** A fork carries its history with it, including
the Linux-specific design decisions. New code can be designed around how
FreeBSD actually works from the first line.

**Compatibility without dependency.** Mocka reimplements MATE's components
so they work with MATE's public interfaces, such as its panel and settings.
You can run Mocka and MATE components side by side while the transition
happens, and move over one piece at a time.

## One component at a time

Mocka replaces MATE gradually until every part has been replaced. The first
component is Mocka Dock, a taskbar-style dock for the panel. The application
menu and a settings tool are next.

## The name

MATE is named after the South American drink, and one of its forks, Café,
kept the tradition going. Mocha is the project founder's favorite treat, so
it felt like the natural next cup. While researching whether any projects
were already called Mocha, he misspelled it with a "k" instead of an "h".
The typo stuck, and Mocha became Mocka.

## Part of GhostBSD

Mocka is developed as part of GhostBSD and ships with it. Development
happens in the open on GitHub, and everyone is welcome to test, report bugs,
and contribute.
