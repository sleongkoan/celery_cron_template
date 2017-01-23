# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

import logging
import shlex
import subprocess

_logger = logging.getLogger(__name__)


class CommandFailed(Exception):
    """Failed to Call the command."""


def call_command(command, pipe=None, echo=False, raise_exc=True):
    """Call bash command."""
    if echo:
        _logger.debug(command)

    process = subprocess.Popen(shlex.split(command.encode("ascii")),
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

    out, err = process.communicate(input=pipe)

    if err and raise_exc:
        raise CommandFailed(
            'Command {} returned stderr: {}'.format(command, err))

    return out, err
