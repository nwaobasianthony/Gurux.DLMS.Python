#
#  --------------------------------------------------------------------------
#   Gurux Ltd
#
#
#
#  Filename: $HeadURL$
#
#  Version: $Revision$,
#                   $Date$
#                   $Author$
#
#  Copyright (c) Gurux Ltd
#
# ---------------------------------------------------------------------------
#
#   DESCRIPTION
#
#  This file is a part of Gurux Device Framework.
#
#  Gurux Device Framework is Open Source software; you can redistribute it
#  and/or modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; version 2 of the License.
#  Gurux Device Framework is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#  See the GNU General Public License for more details.
#
#  More information of Gurux products: http://www.gurux.org
#
#  This code is licensed under the GNU General Public License v2.
#  Full text may be retrieved at http://www.gnu.org/licenses/gpl-2.0.txt
# ---------------------------------------------------------------------------
import sys

#pylint: disable=no-name-in-module
if sys.version_info < (3, 6):
    __base = object
else:
    from enum import IntFlag
    __base = IntFlag

class CreditCollectionConfiguration(__base):
    """
    Defines behavior under specific conditions.
    """
    #pylint: disable=too-few-public-methods

    #
    # None.
    #
    NONE = 0

    #
    # Collect when supply disconnected.
    #
    DISCONNECTED = 0x80

    #
    # Collect in load limiting periods.
    #
    LOAD_LIMITING = 0x40

    #
    # Collect in friendly credit periods.
    #
    FRIENDLY_CREDIT = 0x20
