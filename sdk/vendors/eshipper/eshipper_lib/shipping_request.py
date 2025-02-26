#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Jul 15 10:03:22 2021 by generateDS.py version 2.39.2.
# Python 3.8.6 (v3.8.6:db455296be, Sep 23 2020, 13:31:39)  [Clang 6.0 (clang-600.0.57)]
#
# Command line options:
#   ('--no-namespace-defs', '')
#   ('-o', './eshipper_lib/shipping_request.py')
#
# Command line arguments:
#   ./vendor/schemas/shipping_request.xsd
#
# Command line:
#   /Users/danielkobina/Workspace/project/karrio-bridges/eshipper/.venv/eshipper/bin/generateDS --no-namespace-defs -o "./eshipper_lib/shipping_request.py" ./vendor/schemas/shipping_request.xsd
#
# Current working directory (os.getcwd()):
#   eshipper
#

import sys
try:
    ModulenotfoundExp_ = ModuleNotFoundError
except NameError:
    ModulenotfoundExp_ = ImportError
from six.moves import zip_longest
import os
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_
try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the _exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ModulenotfoundExp_ :
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ModulenotfoundExp_ :
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ModulenotfoundExp_ :

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ModulenotfoundExp_ :
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ModulenotfoundExp_ as exp:
    try:
        from generatedssupersuper import GeneratedsSuperSuper
    except ModulenotfoundExp_ as exp:
        class GeneratedsSuperSuper(object):
            pass
    
    class GeneratedsSuper(GeneratedsSuperSuper):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name
            def utcoffset(self, dt):
                return self.__offset
            def tzname(self, dt):
                return self.__name
            def dst(self, dt):
                return None
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_parse_string(self, input_data, node=None, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node=None, input_name=''):
            if not input_data:
                return ''
            else:
                return input_data
        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data)
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_parse_integer(self, input_data, node=None, input_name=''):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires integer value: %s' % exp)
            return ival
        def gds_validate_integer(self, input_data, node=None, input_name=''):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires integer value')
            return value
        def gds_format_integer_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer values')
            return values
        def gds_format_float(self, input_data, input_name=''):
            return ('%.15f' % input_data).rstrip('0')
        def gds_parse_float(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires float or double value: %s' % exp)
            return fval_
        def gds_validate_float(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires float value')
            return value
        def gds_format_float_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_float_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of float values')
            return values
        def gds_format_decimal(self, input_data, input_name=''):
            return_value = '%s' % input_data
            if '.' in return_value:
                return_value = return_value.rstrip('0')
                if return_value.endswith('.'):
                    return_value = return_value.rstrip('.')
            return return_value
        def gds_parse_decimal(self, input_data, node=None, input_name=''):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return decimal_value
        def gds_validate_decimal(self, input_data, node=None, input_name=''):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return value
        def gds_format_decimal_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return ' '.join([self.gds_format_decimal(item) for item in input_data])
        def gds_validate_decimal_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of decimal values')
            return values
        def gds_format_double(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_parse_double(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires double or float value: %s' % exp)
            return fval_
        def gds_validate_double(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires double or float value')
            return value
        def gds_format_double_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_double_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, 'Requires sequence of double or float values')
            return values
        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()
        def gds_parse_boolean(self, input_data, node=None, input_name=''):
            if input_data in ('true', '1'):
                bval = True
            elif input_data in ('false', '0'):
                bval = False
            else:
                raise_parse_error(node, 'Requires boolean value')
            return bval
        def gds_validate_boolean(self, input_data, node=None, input_name=''):
            if input_data not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires boolean value '
                    '(one of True, 1, False, 0)')
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                value = self.gds_parse_boolean(value, node, input_name)
                if value not in (True, 1, False, 0, ):
                    raise_parse_error(
                        node,
                        'Requires sequence of boolean values '
                        '(one of True, 1, False, 0)')
            return values
        def gds_validate_datetime(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_datetime(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split('.')
            if len(time_parts) > 1:
                micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
                input_data = '%s.%s' % (
                    time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt
        def gds_validate_date(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_date(self, input_data, input_name=''):
            _svalue = '%04d-%02d-%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += 'Z'
                        else:
                            if total_seconds < 0:
                                _svalue += '-'
                                total_seconds *= -1
                            else:
                                _svalue += '+'
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += '{0:02d}:{1:02d}'.format(
                                hours, minutes)
            except AttributeError:
                pass
            return _svalue
        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
            dt = dt.replace(tzinfo=tz)
            return dt.date()
        def gds_validate_time(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_time(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%02d:%02d:%02d' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%02d:%02d:%02d.%s' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1
        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.time()
        def gds_check_cardinality_(
                self, value, input_name,
                min_occurs=0, max_occurs=1, required=None):
            if value is None:
                length = 0
            elif isinstance(value, list):
                length = len(value)
            else:
                length = 1
            if required is not None :
                if required and length < 1:
                    self.gds_collector_.add_message(
                        "Required value {}{} is missing".format(
                            input_name, self.gds_get_node_lineno_()))
            if length < min_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is below "
                    "the minimum allowed, "
                    "expected at least {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        min_occurs, length))
            elif length > max_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is above "
                    "the maximum allowed, "
                    "expected at most {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        max_occurs, length))
        def gds_validate_builtin_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_validate_defined_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content
        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in mapping.items()))
        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = 'utf-8'
                return instring.encode(encoding)
            else:
                return instring
        @staticmethod
        def convert_unicode(instring):
            if isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring, unicode):
                result = quote_xml(instring).encode('utf8')
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result
        def __eq__(self, other):
            def excl_select_objs_(obj):
                return (obj[0] != 'parent_object_' and
                        obj[0] != 'gds_collector_')
            if type(self) != type(other):
                return False
            return all(x == y for x, y in zip_longest(
                filter(excl_select_objs_, self.__dict__.items()),
                filter(excl_select_objs_, other.__dict__.items())))
        def __ne__(self, other):
            return not self.__eq__(other)
        # Django ETL transform hooks.
        def gds_djo_etl_transform(self):
            pass
        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass
        # SQLAlchemy ETL transform hooks.
        def gds_sqa_etl_transform(self):
            return 0, None
        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass
        def gds_get_node_lineno_(self):
            if (hasattr(self, "gds_elementtree_node_") and
                    self.gds_elementtree_node_ is not None):
                return ' near line {}'.format(
                    self.gds_elementtree_node_.sourceline)
            else:
                return ""
    
    
    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + 'Sub'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        if prefix == 'xml':
            namespace = 'http://www.w3.org/XML/1998/namespace'
        else:
            namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))
    def to_etree(self, element, mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self, mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#


class EShipper(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, username=None, password=None, version=None, ShippingRequest=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.username = _cast(None, username)
        self.username_nsprefix_ = None
        self.password = _cast(None, password)
        self.password_nsprefix_ = None
        self.version = _cast(None, version)
        self.version_nsprefix_ = None
        self.ShippingRequest = ShippingRequest
        self.ShippingRequest_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, EShipper)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if EShipper.subclass:
            return EShipper.subclass(*args_, **kwargs_)
        else:
            return EShipper(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ShippingRequest(self):
        return self.ShippingRequest
    def set_ShippingRequest(self, ShippingRequest):
        self.ShippingRequest = ShippingRequest
    def get_username(self):
        return self.username
    def set_username(self, username):
        self.username = username
    def get_password(self):
        return self.password
    def set_password(self, password):
        self.password = password
    def get_version(self):
        return self.version
    def set_version(self, version):
        self.version = version
    def _hasContent(self):
        if (
            self.ShippingRequest is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='EShipper', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('EShipper')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'EShipper':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='EShipper')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='EShipper', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='EShipper'):
        if self.username is not None and 'username' not in already_processed:
            already_processed.add('username')
            outfile.write(' username=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.username), input_name='username')), ))
        if self.password is not None and 'password' not in already_processed:
            already_processed.add('password')
            outfile.write(' password=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.password), input_name='password')), ))
        if self.version is not None and 'version' not in already_processed:
            already_processed.add('version')
            outfile.write(' version=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.version), input_name='version')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='EShipper', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ShippingRequest is not None:
            namespaceprefix_ = self.ShippingRequest_nsprefix_ + ':' if (UseCapturedNS_ and self.ShippingRequest_nsprefix_) else ''
            self.ShippingRequest.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ShippingRequest', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('username', node)
        if value is not None and 'username' not in already_processed:
            already_processed.add('username')
            self.username = value
        value = find_attr_value_('password', node)
        if value is not None and 'password' not in already_processed:
            already_processed.add('password')
            self.password = value
        value = find_attr_value_('version', node)
        if value is not None and 'version' not in already_processed:
            already_processed.add('version')
            self.version = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ShippingRequest':
            obj_ = ShippingRequestType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ShippingRequest = obj_
            obj_.original_tagname_ = 'ShippingRequest'
# end class EShipper


class ShippingRequestType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, serviceId=None, destinationCloseMin=None, destinationCloseHrs=None, originCloseTimeMin=None, originCloseTimeHrs=None, readyTimeMin=None, readyTimeHrs=None, SortandSegregateCharge=None, homelandSecurity=None, pierCharge=None, exhibitionConventionSite=None, militaryBaseDelivery=None, customsIn_bondFreight=None, limitedAccess=None, excessLength=None, crossBorderFee=None, singleShipment=None, insidePickup=None, insuranceType=None, scheduledShipDate=None, insideDelivery=None, deliveryAppointment=None, specialEquipment=None, holdForPickupRequired=None, signatureRequired=None, isSaturdayService=None, dangerousGoodsType=None, stackable=None, From=None, To=None, Shipper=None, COD=None, Packages=None, Pickup=None, Payment=None, Reference=None, CustomsInvoice=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.serviceId = _cast(int, serviceId)
        self.serviceId_nsprefix_ = None
        self.destinationCloseMin = _cast(None, destinationCloseMin)
        self.destinationCloseMin_nsprefix_ = None
        self.destinationCloseHrs = _cast(None, destinationCloseHrs)
        self.destinationCloseHrs_nsprefix_ = None
        self.originCloseTimeMin = _cast(None, originCloseTimeMin)
        self.originCloseTimeMin_nsprefix_ = None
        self.originCloseTimeHrs = _cast(None, originCloseTimeHrs)
        self.originCloseTimeHrs_nsprefix_ = None
        self.readyTimeMin = _cast(None, readyTimeMin)
        self.readyTimeMin_nsprefix_ = None
        self.readyTimeHrs = _cast(None, readyTimeHrs)
        self.readyTimeHrs_nsprefix_ = None
        self.SortandSegregateCharge = _cast(None, SortandSegregateCharge)
        self.SortandSegregateCharge_nsprefix_ = None
        self.homelandSecurity = _cast(None, homelandSecurity)
        self.homelandSecurity_nsprefix_ = None
        self.pierCharge = _cast(None, pierCharge)
        self.pierCharge_nsprefix_ = None
        self.exhibitionConventionSite = _cast(None, exhibitionConventionSite)
        self.exhibitionConventionSite_nsprefix_ = None
        self.militaryBaseDelivery = _cast(None, militaryBaseDelivery)
        self.militaryBaseDelivery_nsprefix_ = None
        self.customsIn_bondFreight = _cast(None, customsIn_bondFreight)
        self.customsIn_bondFreight_nsprefix_ = None
        self.limitedAccess = _cast(None, limitedAccess)
        self.limitedAccess_nsprefix_ = None
        self.excessLength = _cast(None, excessLength)
        self.excessLength_nsprefix_ = None
        self.crossBorderFee = _cast(None, crossBorderFee)
        self.crossBorderFee_nsprefix_ = None
        self.singleShipment = _cast(None, singleShipment)
        self.singleShipment_nsprefix_ = None
        self.insidePickup = _cast(None, insidePickup)
        self.insidePickup_nsprefix_ = None
        self.insuranceType = _cast(None, insuranceType)
        self.insuranceType_nsprefix_ = None
        self.scheduledShipDate = _cast(None, scheduledShipDate)
        self.scheduledShipDate_nsprefix_ = None
        self.insideDelivery = _cast(None, insideDelivery)
        self.insideDelivery_nsprefix_ = None
        self.deliveryAppointment = _cast(None, deliveryAppointment)
        self.deliveryAppointment_nsprefix_ = None
        self.specialEquipment = _cast(None, specialEquipment)
        self.specialEquipment_nsprefix_ = None
        self.holdForPickupRequired = _cast(None, holdForPickupRequired)
        self.holdForPickupRequired_nsprefix_ = None
        self.signatureRequired = _cast(None, signatureRequired)
        self.signatureRequired_nsprefix_ = None
        self.isSaturdayService = _cast(None, isSaturdayService)
        self.isSaturdayService_nsprefix_ = None
        self.dangerousGoodsType = _cast(None, dangerousGoodsType)
        self.dangerousGoodsType_nsprefix_ = None
        self.stackable = _cast(None, stackable)
        self.stackable_nsprefix_ = None
        self.From = From
        self.From_nsprefix_ = None
        self.To = To
        self.To_nsprefix_ = None
        self.Shipper = Shipper
        self.Shipper_nsprefix_ = None
        self.COD = COD
        self.COD_nsprefix_ = None
        self.Packages = Packages
        self.Packages_nsprefix_ = None
        self.Pickup = Pickup
        self.Pickup_nsprefix_ = None
        self.Payment = Payment
        self.Payment_nsprefix_ = None
        if Reference is None:
            self.Reference = []
        else:
            self.Reference = Reference
        self.Reference_nsprefix_ = None
        self.CustomsInvoice = CustomsInvoice
        self.CustomsInvoice_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ShippingRequestType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ShippingRequestType.subclass:
            return ShippingRequestType.subclass(*args_, **kwargs_)
        else:
            return ShippingRequestType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_From(self):
        return self.From
    def set_From(self, From):
        self.From = From
    def get_To(self):
        return self.To
    def set_To(self, To):
        self.To = To
    def get_Shipper(self):
        return self.Shipper
    def set_Shipper(self, Shipper):
        self.Shipper = Shipper
    def get_COD(self):
        return self.COD
    def set_COD(self, COD):
        self.COD = COD
    def get_Packages(self):
        return self.Packages
    def set_Packages(self, Packages):
        self.Packages = Packages
    def get_Pickup(self):
        return self.Pickup
    def set_Pickup(self, Pickup):
        self.Pickup = Pickup
    def get_Payment(self):
        return self.Payment
    def set_Payment(self, Payment):
        self.Payment = Payment
    def get_Reference(self):
        return self.Reference
    def set_Reference(self, Reference):
        self.Reference = Reference
    def add_Reference(self, value):
        self.Reference.append(value)
    def insert_Reference_at(self, index, value):
        self.Reference.insert(index, value)
    def replace_Reference_at(self, index, value):
        self.Reference[index] = value
    def get_CustomsInvoice(self):
        return self.CustomsInvoice
    def set_CustomsInvoice(self, CustomsInvoice):
        self.CustomsInvoice = CustomsInvoice
    def get_serviceId(self):
        return self.serviceId
    def set_serviceId(self, serviceId):
        self.serviceId = serviceId
    def get_destinationCloseMin(self):
        return self.destinationCloseMin
    def set_destinationCloseMin(self, destinationCloseMin):
        self.destinationCloseMin = destinationCloseMin
    def get_destinationCloseHrs(self):
        return self.destinationCloseHrs
    def set_destinationCloseHrs(self, destinationCloseHrs):
        self.destinationCloseHrs = destinationCloseHrs
    def get_originCloseTimeMin(self):
        return self.originCloseTimeMin
    def set_originCloseTimeMin(self, originCloseTimeMin):
        self.originCloseTimeMin = originCloseTimeMin
    def get_originCloseTimeHrs(self):
        return self.originCloseTimeHrs
    def set_originCloseTimeHrs(self, originCloseTimeHrs):
        self.originCloseTimeHrs = originCloseTimeHrs
    def get_readyTimeMin(self):
        return self.readyTimeMin
    def set_readyTimeMin(self, readyTimeMin):
        self.readyTimeMin = readyTimeMin
    def get_readyTimeHrs(self):
        return self.readyTimeHrs
    def set_readyTimeHrs(self, readyTimeHrs):
        self.readyTimeHrs = readyTimeHrs
    def get_SortandSegregateCharge(self):
        return self.SortandSegregateCharge
    def set_SortandSegregateCharge(self, SortandSegregateCharge):
        self.SortandSegregateCharge = SortandSegregateCharge
    def get_homelandSecurity(self):
        return self.homelandSecurity
    def set_homelandSecurity(self, homelandSecurity):
        self.homelandSecurity = homelandSecurity
    def get_pierCharge(self):
        return self.pierCharge
    def set_pierCharge(self, pierCharge):
        self.pierCharge = pierCharge
    def get_exhibitionConventionSite(self):
        return self.exhibitionConventionSite
    def set_exhibitionConventionSite(self, exhibitionConventionSite):
        self.exhibitionConventionSite = exhibitionConventionSite
    def get_militaryBaseDelivery(self):
        return self.militaryBaseDelivery
    def set_militaryBaseDelivery(self, militaryBaseDelivery):
        self.militaryBaseDelivery = militaryBaseDelivery
    def get_customsIn_bondFreight(self):
        return self.customsIn_bondFreight
    def set_customsIn_bondFreight(self, customsIn_bondFreight):
        self.customsIn_bondFreight = customsIn_bondFreight
    def get_limitedAccess(self):
        return self.limitedAccess
    def set_limitedAccess(self, limitedAccess):
        self.limitedAccess = limitedAccess
    def get_excessLength(self):
        return self.excessLength
    def set_excessLength(self, excessLength):
        self.excessLength = excessLength
    def get_crossBorderFee(self):
        return self.crossBorderFee
    def set_crossBorderFee(self, crossBorderFee):
        self.crossBorderFee = crossBorderFee
    def get_singleShipment(self):
        return self.singleShipment
    def set_singleShipment(self, singleShipment):
        self.singleShipment = singleShipment
    def get_insidePickup(self):
        return self.insidePickup
    def set_insidePickup(self, insidePickup):
        self.insidePickup = insidePickup
    def get_insuranceType(self):
        return self.insuranceType
    def set_insuranceType(self, insuranceType):
        self.insuranceType = insuranceType
    def get_scheduledShipDate(self):
        return self.scheduledShipDate
    def set_scheduledShipDate(self, scheduledShipDate):
        self.scheduledShipDate = scheduledShipDate
    def get_insideDelivery(self):
        return self.insideDelivery
    def set_insideDelivery(self, insideDelivery):
        self.insideDelivery = insideDelivery
    def get_deliveryAppointment(self):
        return self.deliveryAppointment
    def set_deliveryAppointment(self, deliveryAppointment):
        self.deliveryAppointment = deliveryAppointment
    def get_specialEquipment(self):
        return self.specialEquipment
    def set_specialEquipment(self, specialEquipment):
        self.specialEquipment = specialEquipment
    def get_holdForPickupRequired(self):
        return self.holdForPickupRequired
    def set_holdForPickupRequired(self, holdForPickupRequired):
        self.holdForPickupRequired = holdForPickupRequired
    def get_signatureRequired(self):
        return self.signatureRequired
    def set_signatureRequired(self, signatureRequired):
        self.signatureRequired = signatureRequired
    def get_isSaturdayService(self):
        return self.isSaturdayService
    def set_isSaturdayService(self, isSaturdayService):
        self.isSaturdayService = isSaturdayService
    def get_dangerousGoodsType(self):
        return self.dangerousGoodsType
    def set_dangerousGoodsType(self, dangerousGoodsType):
        self.dangerousGoodsType = dangerousGoodsType
    def get_stackable(self):
        return self.stackable
    def set_stackable(self, stackable):
        self.stackable = stackable
    def _hasContent(self):
        if (
            self.From is not None or
            self.To is not None or
            self.Shipper is not None or
            self.COD is not None or
            self.Packages is not None or
            self.Pickup is not None or
            self.Payment is not None or
            self.Reference or
            self.CustomsInvoice is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShippingRequestType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ShippingRequestType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ShippingRequestType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ShippingRequestType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ShippingRequestType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ShippingRequestType'):
        if self.serviceId is not None and 'serviceId' not in already_processed:
            already_processed.add('serviceId')
            outfile.write(' serviceId="%s"' % self.gds_format_integer(self.serviceId, input_name='serviceId'))
        if self.destinationCloseMin is not None and 'destinationCloseMin' not in already_processed:
            already_processed.add('destinationCloseMin')
            outfile.write(' destinationCloseMin=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.destinationCloseMin), input_name='destinationCloseMin')), ))
        if self.destinationCloseHrs is not None and 'destinationCloseHrs' not in already_processed:
            already_processed.add('destinationCloseHrs')
            outfile.write(' destinationCloseHrs=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.destinationCloseHrs), input_name='destinationCloseHrs')), ))
        if self.originCloseTimeMin is not None and 'originCloseTimeMin' not in already_processed:
            already_processed.add('originCloseTimeMin')
            outfile.write(' originCloseTimeMin=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.originCloseTimeMin), input_name='originCloseTimeMin')), ))
        if self.originCloseTimeHrs is not None and 'originCloseTimeHrs' not in already_processed:
            already_processed.add('originCloseTimeHrs')
            outfile.write(' originCloseTimeHrs=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.originCloseTimeHrs), input_name='originCloseTimeHrs')), ))
        if self.readyTimeMin is not None and 'readyTimeMin' not in already_processed:
            already_processed.add('readyTimeMin')
            outfile.write(' readyTimeMin=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.readyTimeMin), input_name='readyTimeMin')), ))
        if self.readyTimeHrs is not None and 'readyTimeHrs' not in already_processed:
            already_processed.add('readyTimeHrs')
            outfile.write(' readyTimeHrs=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.readyTimeHrs), input_name='readyTimeHrs')), ))
        if self.SortandSegregateCharge is not None and 'SortandSegregateCharge' not in already_processed:
            already_processed.add('SortandSegregateCharge')
            outfile.write(' SortandSegregateCharge=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.SortandSegregateCharge), input_name='SortandSegregateCharge')), ))
        if self.homelandSecurity is not None and 'homelandSecurity' not in already_processed:
            already_processed.add('homelandSecurity')
            outfile.write(' homelandSecurity=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.homelandSecurity), input_name='homelandSecurity')), ))
        if self.pierCharge is not None and 'pierCharge' not in already_processed:
            already_processed.add('pierCharge')
            outfile.write(' pierCharge=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.pierCharge), input_name='pierCharge')), ))
        if self.exhibitionConventionSite is not None and 'exhibitionConventionSite' not in already_processed:
            already_processed.add('exhibitionConventionSite')
            outfile.write(' exhibitionConventionSite=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.exhibitionConventionSite), input_name='exhibitionConventionSite')), ))
        if self.militaryBaseDelivery is not None and 'militaryBaseDelivery' not in already_processed:
            already_processed.add('militaryBaseDelivery')
            outfile.write(' militaryBaseDelivery=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.militaryBaseDelivery), input_name='militaryBaseDelivery')), ))
        if self.customsIn_bondFreight is not None and 'customsIn_bondFreight' not in already_processed:
            already_processed.add('customsIn_bondFreight')
            outfile.write(' customsIn-bondFreight=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.customsIn_bondFreight), input_name='customsIn-bondFreight')), ))
        if self.limitedAccess is not None and 'limitedAccess' not in already_processed:
            already_processed.add('limitedAccess')
            outfile.write(' limitedAccess=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.limitedAccess), input_name='limitedAccess')), ))
        if self.excessLength is not None and 'excessLength' not in already_processed:
            already_processed.add('excessLength')
            outfile.write(' excessLength=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.excessLength), input_name='excessLength')), ))
        if self.crossBorderFee is not None and 'crossBorderFee' not in already_processed:
            already_processed.add('crossBorderFee')
            outfile.write(' crossBorderFee=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.crossBorderFee), input_name='crossBorderFee')), ))
        if self.singleShipment is not None and 'singleShipment' not in already_processed:
            already_processed.add('singleShipment')
            outfile.write(' singleShipment=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.singleShipment), input_name='singleShipment')), ))
        if self.insidePickup is not None and 'insidePickup' not in already_processed:
            already_processed.add('insidePickup')
            outfile.write(' insidePickup=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.insidePickup), input_name='insidePickup')), ))
        if self.insuranceType is not None and 'insuranceType' not in already_processed:
            already_processed.add('insuranceType')
            outfile.write(' insuranceType=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.insuranceType), input_name='insuranceType')), ))
        if self.scheduledShipDate is not None and 'scheduledShipDate' not in already_processed:
            already_processed.add('scheduledShipDate')
            outfile.write(' scheduledShipDate=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.scheduledShipDate), input_name='scheduledShipDate')), ))
        if self.insideDelivery is not None and 'insideDelivery' not in already_processed:
            already_processed.add('insideDelivery')
            outfile.write(' insideDelivery=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.insideDelivery), input_name='insideDelivery')), ))
        if self.deliveryAppointment is not None and 'deliveryAppointment' not in already_processed:
            already_processed.add('deliveryAppointment')
            outfile.write(' deliveryAppointment=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.deliveryAppointment), input_name='deliveryAppointment')), ))
        if self.specialEquipment is not None and 'specialEquipment' not in already_processed:
            already_processed.add('specialEquipment')
            outfile.write(' specialEquipment=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.specialEquipment), input_name='specialEquipment')), ))
        if self.holdForPickupRequired is not None and 'holdForPickupRequired' not in already_processed:
            already_processed.add('holdForPickupRequired')
            outfile.write(' holdForPickupRequired=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.holdForPickupRequired), input_name='holdForPickupRequired')), ))
        if self.signatureRequired is not None and 'signatureRequired' not in already_processed:
            already_processed.add('signatureRequired')
            outfile.write(' signatureRequired=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.signatureRequired), input_name='signatureRequired')), ))
        if self.isSaturdayService is not None and 'isSaturdayService' not in already_processed:
            already_processed.add('isSaturdayService')
            outfile.write(' isSaturdayService=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.isSaturdayService), input_name='isSaturdayService')), ))
        if self.dangerousGoodsType is not None and 'dangerousGoodsType' not in already_processed:
            already_processed.add('dangerousGoodsType')
            outfile.write(' dangerousGoodsType=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.dangerousGoodsType), input_name='dangerousGoodsType')), ))
        if self.stackable is not None and 'stackable' not in already_processed:
            already_processed.add('stackable')
            outfile.write(' stackable=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.stackable), input_name='stackable')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShippingRequestType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.From is not None:
            namespaceprefix_ = self.From_nsprefix_ + ':' if (UseCapturedNS_ and self.From_nsprefix_) else ''
            self.From.export(outfile, level, namespaceprefix_, namespacedef_='', name_='From', pretty_print=pretty_print)
        if self.To is not None:
            namespaceprefix_ = self.To_nsprefix_ + ':' if (UseCapturedNS_ and self.To_nsprefix_) else ''
            self.To.export(outfile, level, namespaceprefix_, namespacedef_='', name_='To', pretty_print=pretty_print)
        if self.Shipper is not None:
            namespaceprefix_ = self.Shipper_nsprefix_ + ':' if (UseCapturedNS_ and self.Shipper_nsprefix_) else ''
            self.Shipper.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Shipper', pretty_print=pretty_print)
        if self.COD is not None:
            namespaceprefix_ = self.COD_nsprefix_ + ':' if (UseCapturedNS_ and self.COD_nsprefix_) else ''
            self.COD.export(outfile, level, namespaceprefix_, namespacedef_='', name_='COD', pretty_print=pretty_print)
        if self.Packages is not None:
            namespaceprefix_ = self.Packages_nsprefix_ + ':' if (UseCapturedNS_ and self.Packages_nsprefix_) else ''
            self.Packages.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Packages', pretty_print=pretty_print)
        if self.Pickup is not None:
            namespaceprefix_ = self.Pickup_nsprefix_ + ':' if (UseCapturedNS_ and self.Pickup_nsprefix_) else ''
            self.Pickup.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Pickup', pretty_print=pretty_print)
        if self.Payment is not None:
            namespaceprefix_ = self.Payment_nsprefix_ + ':' if (UseCapturedNS_ and self.Payment_nsprefix_) else ''
            self.Payment.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Payment', pretty_print=pretty_print)
        for Reference_ in self.Reference:
            namespaceprefix_ = self.Reference_nsprefix_ + ':' if (UseCapturedNS_ and self.Reference_nsprefix_) else ''
            Reference_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Reference', pretty_print=pretty_print)
        if self.CustomsInvoice is not None:
            namespaceprefix_ = self.CustomsInvoice_nsprefix_ + ':' if (UseCapturedNS_ and self.CustomsInvoice_nsprefix_) else ''
            self.CustomsInvoice.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CustomsInvoice', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('serviceId', node)
        if value is not None and 'serviceId' not in already_processed:
            already_processed.add('serviceId')
            self.serviceId = self.gds_parse_integer(value, node, 'serviceId')
        value = find_attr_value_('destinationCloseMin', node)
        if value is not None and 'destinationCloseMin' not in already_processed:
            already_processed.add('destinationCloseMin')
            self.destinationCloseMin = value
        value = find_attr_value_('destinationCloseHrs', node)
        if value is not None and 'destinationCloseHrs' not in already_processed:
            already_processed.add('destinationCloseHrs')
            self.destinationCloseHrs = value
        value = find_attr_value_('originCloseTimeMin', node)
        if value is not None and 'originCloseTimeMin' not in already_processed:
            already_processed.add('originCloseTimeMin')
            self.originCloseTimeMin = value
        value = find_attr_value_('originCloseTimeHrs', node)
        if value is not None and 'originCloseTimeHrs' not in already_processed:
            already_processed.add('originCloseTimeHrs')
            self.originCloseTimeHrs = value
        value = find_attr_value_('readyTimeMin', node)
        if value is not None and 'readyTimeMin' not in already_processed:
            already_processed.add('readyTimeMin')
            self.readyTimeMin = value
        value = find_attr_value_('readyTimeHrs', node)
        if value is not None and 'readyTimeHrs' not in already_processed:
            already_processed.add('readyTimeHrs')
            self.readyTimeHrs = value
        value = find_attr_value_('SortandSegregateCharge', node)
        if value is not None and 'SortandSegregateCharge' not in already_processed:
            already_processed.add('SortandSegregateCharge')
            self.SortandSegregateCharge = value
        value = find_attr_value_('homelandSecurity', node)
        if value is not None and 'homelandSecurity' not in already_processed:
            already_processed.add('homelandSecurity')
            self.homelandSecurity = value
        value = find_attr_value_('pierCharge', node)
        if value is not None and 'pierCharge' not in already_processed:
            already_processed.add('pierCharge')
            self.pierCharge = value
        value = find_attr_value_('exhibitionConventionSite', node)
        if value is not None and 'exhibitionConventionSite' not in already_processed:
            already_processed.add('exhibitionConventionSite')
            self.exhibitionConventionSite = value
        value = find_attr_value_('militaryBaseDelivery', node)
        if value is not None and 'militaryBaseDelivery' not in already_processed:
            already_processed.add('militaryBaseDelivery')
            self.militaryBaseDelivery = value
        value = find_attr_value_('customsIn-bondFreight', node)
        if value is not None and 'customsIn-bondFreight' not in already_processed:
            already_processed.add('customsIn-bondFreight')
            self.customsIn_bondFreight = value
        value = find_attr_value_('limitedAccess', node)
        if value is not None and 'limitedAccess' not in already_processed:
            already_processed.add('limitedAccess')
            self.limitedAccess = value
        value = find_attr_value_('excessLength', node)
        if value is not None and 'excessLength' not in already_processed:
            already_processed.add('excessLength')
            self.excessLength = value
        value = find_attr_value_('crossBorderFee', node)
        if value is not None and 'crossBorderFee' not in already_processed:
            already_processed.add('crossBorderFee')
            self.crossBorderFee = value
        value = find_attr_value_('singleShipment', node)
        if value is not None and 'singleShipment' not in already_processed:
            already_processed.add('singleShipment')
            self.singleShipment = value
        value = find_attr_value_('insidePickup', node)
        if value is not None and 'insidePickup' not in already_processed:
            already_processed.add('insidePickup')
            self.insidePickup = value
        value = find_attr_value_('insuranceType', node)
        if value is not None and 'insuranceType' not in already_processed:
            already_processed.add('insuranceType')
            self.insuranceType = value
        value = find_attr_value_('scheduledShipDate', node)
        if value is not None and 'scheduledShipDate' not in already_processed:
            already_processed.add('scheduledShipDate')
            self.scheduledShipDate = value
        value = find_attr_value_('insideDelivery', node)
        if value is not None and 'insideDelivery' not in already_processed:
            already_processed.add('insideDelivery')
            self.insideDelivery = value
        value = find_attr_value_('deliveryAppointment', node)
        if value is not None and 'deliveryAppointment' not in already_processed:
            already_processed.add('deliveryAppointment')
            self.deliveryAppointment = value
        value = find_attr_value_('specialEquipment', node)
        if value is not None and 'specialEquipment' not in already_processed:
            already_processed.add('specialEquipment')
            self.specialEquipment = value
        value = find_attr_value_('holdForPickupRequired', node)
        if value is not None and 'holdForPickupRequired' not in already_processed:
            already_processed.add('holdForPickupRequired')
            self.holdForPickupRequired = value
        value = find_attr_value_('signatureRequired', node)
        if value is not None and 'signatureRequired' not in already_processed:
            already_processed.add('signatureRequired')
            self.signatureRequired = value
        value = find_attr_value_('isSaturdayService', node)
        if value is not None and 'isSaturdayService' not in already_processed:
            already_processed.add('isSaturdayService')
            self.isSaturdayService = value
        value = find_attr_value_('dangerousGoodsType', node)
        if value is not None and 'dangerousGoodsType' not in already_processed:
            already_processed.add('dangerousGoodsType')
            self.dangerousGoodsType = value
        value = find_attr_value_('stackable', node)
        if value is not None and 'stackable' not in already_processed:
            already_processed.add('stackable')
            self.stackable = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'From':
            obj_ = FromType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.From = obj_
            obj_.original_tagname_ = 'From'
        elif nodeName_ == 'To':
            obj_ = ToType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.To = obj_
            obj_.original_tagname_ = 'To'
        elif nodeName_ == 'Shipper':
            obj_ = ShipperType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Shipper = obj_
            obj_.original_tagname_ = 'Shipper'
        elif nodeName_ == 'COD':
            obj_ = CODType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.COD = obj_
            obj_.original_tagname_ = 'COD'
        elif nodeName_ == 'Packages':
            obj_ = PackagesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Packages = obj_
            obj_.original_tagname_ = 'Packages'
        elif nodeName_ == 'Pickup':
            obj_ = PickupType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Pickup = obj_
            obj_.original_tagname_ = 'Pickup'
        elif nodeName_ == 'Payment':
            obj_ = PaymentType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Payment = obj_
            obj_.original_tagname_ = 'Payment'
        elif nodeName_ == 'Reference':
            obj_ = ReferenceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Reference.append(obj_)
            obj_.original_tagname_ = 'Reference'
        elif nodeName_ == 'CustomsInvoice':
            obj_ = CustomsInvoiceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CustomsInvoice = obj_
            obj_.original_tagname_ = 'CustomsInvoice'
# end class ShippingRequestType


class FromType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, company=None, email=None, attention=None, phone=None, tailgateRequired=None, residential=None, confirmDelivery=None, instructions=None, address1=None, address2=None, city=None, state=None, country=None, zip=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.company = _cast(None, company)
        self.company_nsprefix_ = None
        self.email = _cast(None, email)
        self.email_nsprefix_ = None
        self.attention = _cast(None, attention)
        self.attention_nsprefix_ = None
        self.phone = _cast(None, phone)
        self.phone_nsprefix_ = None
        self.tailgateRequired = _cast(None, tailgateRequired)
        self.tailgateRequired_nsprefix_ = None
        self.residential = _cast(None, residential)
        self.residential_nsprefix_ = None
        self.confirmDelivery = _cast(None, confirmDelivery)
        self.confirmDelivery_nsprefix_ = None
        self.instructions = _cast(None, instructions)
        self.instructions_nsprefix_ = None
        self.address1 = _cast(None, address1)
        self.address1_nsprefix_ = None
        self.address2 = _cast(None, address2)
        self.address2_nsprefix_ = None
        self.city = _cast(None, city)
        self.city_nsprefix_ = None
        self.state = _cast(None, state)
        self.state_nsprefix_ = None
        self.country = _cast(None, country)
        self.country_nsprefix_ = None
        self.zip = _cast(None, zip)
        self.zip_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, FromType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if FromType.subclass:
            return FromType.subclass(*args_, **kwargs_)
        else:
            return FromType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_company(self):
        return self.company
    def set_company(self, company):
        self.company = company
    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email = email
    def get_attention(self):
        return self.attention
    def set_attention(self, attention):
        self.attention = attention
    def get_phone(self):
        return self.phone
    def set_phone(self, phone):
        self.phone = phone
    def get_tailgateRequired(self):
        return self.tailgateRequired
    def set_tailgateRequired(self, tailgateRequired):
        self.tailgateRequired = tailgateRequired
    def get_residential(self):
        return self.residential
    def set_residential(self, residential):
        self.residential = residential
    def get_confirmDelivery(self):
        return self.confirmDelivery
    def set_confirmDelivery(self, confirmDelivery):
        self.confirmDelivery = confirmDelivery
    def get_instructions(self):
        return self.instructions
    def set_instructions(self, instructions):
        self.instructions = instructions
    def get_address1(self):
        return self.address1
    def set_address1(self, address1):
        self.address1 = address1
    def get_address2(self):
        return self.address2
    def set_address2(self, address2):
        self.address2 = address2
    def get_city(self):
        return self.city
    def set_city(self, city):
        self.city = city
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
    def get_country(self):
        return self.country
    def set_country(self, country):
        self.country = country
    def get_zip(self):
        return self.zip
    def set_zip(self, zip):
        self.zip = zip
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='FromType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('FromType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'FromType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='FromType')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='FromType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='FromType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
        if self.company is not None and 'company' not in already_processed:
            already_processed.add('company')
            outfile.write(' company=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.company), input_name='company')), ))
        if self.email is not None and 'email' not in already_processed:
            already_processed.add('email')
            outfile.write(' email=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.email), input_name='email')), ))
        if self.attention is not None and 'attention' not in already_processed:
            already_processed.add('attention')
            outfile.write(' attention=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.attention), input_name='attention')), ))
        if self.phone is not None and 'phone' not in already_processed:
            already_processed.add('phone')
            outfile.write(' phone=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.phone), input_name='phone')), ))
        if self.tailgateRequired is not None and 'tailgateRequired' not in already_processed:
            already_processed.add('tailgateRequired')
            outfile.write(' tailgateRequired=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.tailgateRequired), input_name='tailgateRequired')), ))
        if self.residential is not None and 'residential' not in already_processed:
            already_processed.add('residential')
            outfile.write(' residential=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.residential), input_name='residential')), ))
        if self.confirmDelivery is not None and 'confirmDelivery' not in already_processed:
            already_processed.add('confirmDelivery')
            outfile.write(' confirmDelivery=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.confirmDelivery), input_name='confirmDelivery')), ))
        if self.instructions is not None and 'instructions' not in already_processed:
            already_processed.add('instructions')
            outfile.write(' instructions=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.instructions), input_name='instructions')), ))
        if self.address1 is not None and 'address1' not in already_processed:
            already_processed.add('address1')
            outfile.write(' address1=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.address1), input_name='address1')), ))
        if self.address2 is not None and 'address2' not in already_processed:
            already_processed.add('address2')
            outfile.write(' address2=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.address2), input_name='address2')), ))
        if self.city is not None and 'city' not in already_processed:
            already_processed.add('city')
            outfile.write(' city=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.city), input_name='city')), ))
        if self.state is not None and 'state' not in already_processed:
            already_processed.add('state')
            outfile.write(' state=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.state), input_name='state')), ))
        if self.country is not None and 'country' not in already_processed:
            already_processed.add('country')
            outfile.write(' country=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.country), input_name='country')), ))
        if self.zip is not None and 'zip' not in already_processed:
            already_processed.add('zip')
            outfile.write(' zip=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.zip), input_name='zip')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='FromType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('company', node)
        if value is not None and 'company' not in already_processed:
            already_processed.add('company')
            self.company = value
        value = find_attr_value_('email', node)
        if value is not None and 'email' not in already_processed:
            already_processed.add('email')
            self.email = value
        value = find_attr_value_('attention', node)
        if value is not None and 'attention' not in already_processed:
            already_processed.add('attention')
            self.attention = value
        value = find_attr_value_('phone', node)
        if value is not None and 'phone' not in already_processed:
            already_processed.add('phone')
            self.phone = value
        value = find_attr_value_('tailgateRequired', node)
        if value is not None and 'tailgateRequired' not in already_processed:
            already_processed.add('tailgateRequired')
            self.tailgateRequired = value
        value = find_attr_value_('residential', node)
        if value is not None and 'residential' not in already_processed:
            already_processed.add('residential')
            self.residential = value
        value = find_attr_value_('confirmDelivery', node)
        if value is not None and 'confirmDelivery' not in already_processed:
            already_processed.add('confirmDelivery')
            self.confirmDelivery = value
        value = find_attr_value_('instructions', node)
        if value is not None and 'instructions' not in already_processed:
            already_processed.add('instructions')
            self.instructions = value
        value = find_attr_value_('address1', node)
        if value is not None and 'address1' not in already_processed:
            already_processed.add('address1')
            self.address1 = value
        value = find_attr_value_('address2', node)
        if value is not None and 'address2' not in already_processed:
            already_processed.add('address2')
            self.address2 = value
        value = find_attr_value_('city', node)
        if value is not None and 'city' not in already_processed:
            already_processed.add('city')
            self.city = value
        value = find_attr_value_('state', node)
        if value is not None and 'state' not in already_processed:
            already_processed.add('state')
            self.state = value
        value = find_attr_value_('country', node)
        if value is not None and 'country' not in already_processed:
            already_processed.add('country')
            self.country = value
        value = find_attr_value_('zip', node)
        if value is not None and 'zip' not in already_processed:
            already_processed.add('zip')
            self.zip = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class FromType


class ToType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, company=None, email=None, notifyRecipient=None, attention=None, phone=None, tailgateRequired=None, residential=None, instructions=None, address1=None, address2=None, city=None, state=None, country=None, zip=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.company = _cast(None, company)
        self.company_nsprefix_ = None
        self.email = _cast(None, email)
        self.email_nsprefix_ = None
        self.notifyRecipient = _cast(None, notifyRecipient)
        self.notifyRecipient_nsprefix_ = None
        self.attention = _cast(None, attention)
        self.attention_nsprefix_ = None
        self.phone = _cast(None, phone)
        self.phone_nsprefix_ = None
        self.tailgateRequired = _cast(None, tailgateRequired)
        self.tailgateRequired_nsprefix_ = None
        self.residential = _cast(None, residential)
        self.residential_nsprefix_ = None
        self.instructions = _cast(None, instructions)
        self.instructions_nsprefix_ = None
        self.address1 = _cast(None, address1)
        self.address1_nsprefix_ = None
        self.address2 = _cast(None, address2)
        self.address2_nsprefix_ = None
        self.city = _cast(None, city)
        self.city_nsprefix_ = None
        self.state = _cast(None, state)
        self.state_nsprefix_ = None
        self.country = _cast(None, country)
        self.country_nsprefix_ = None
        self.zip = _cast(None, zip)
        self.zip_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ToType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ToType.subclass:
            return ToType.subclass(*args_, **kwargs_)
        else:
            return ToType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_company(self):
        return self.company
    def set_company(self, company):
        self.company = company
    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email = email
    def get_notifyRecipient(self):
        return self.notifyRecipient
    def set_notifyRecipient(self, notifyRecipient):
        self.notifyRecipient = notifyRecipient
    def get_attention(self):
        return self.attention
    def set_attention(self, attention):
        self.attention = attention
    def get_phone(self):
        return self.phone
    def set_phone(self, phone):
        self.phone = phone
    def get_tailgateRequired(self):
        return self.tailgateRequired
    def set_tailgateRequired(self, tailgateRequired):
        self.tailgateRequired = tailgateRequired
    def get_residential(self):
        return self.residential
    def set_residential(self, residential):
        self.residential = residential
    def get_instructions(self):
        return self.instructions
    def set_instructions(self, instructions):
        self.instructions = instructions
    def get_address1(self):
        return self.address1
    def set_address1(self, address1):
        self.address1 = address1
    def get_address2(self):
        return self.address2
    def set_address2(self, address2):
        self.address2 = address2
    def get_city(self):
        return self.city
    def set_city(self, city):
        self.city = city
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
    def get_country(self):
        return self.country
    def set_country(self, country):
        self.country = country
    def get_zip(self):
        return self.zip
    def set_zip(self, zip):
        self.zip = zip
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ToType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ToType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ToType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ToType')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ToType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ToType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
        if self.company is not None and 'company' not in already_processed:
            already_processed.add('company')
            outfile.write(' company=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.company), input_name='company')), ))
        if self.email is not None and 'email' not in already_processed:
            already_processed.add('email')
            outfile.write(' email=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.email), input_name='email')), ))
        if self.notifyRecipient is not None and 'notifyRecipient' not in already_processed:
            already_processed.add('notifyRecipient')
            outfile.write(' notifyRecipient=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.notifyRecipient), input_name='notifyRecipient')), ))
        if self.attention is not None and 'attention' not in already_processed:
            already_processed.add('attention')
            outfile.write(' attention=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.attention), input_name='attention')), ))
        if self.phone is not None and 'phone' not in already_processed:
            already_processed.add('phone')
            outfile.write(' phone=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.phone), input_name='phone')), ))
        if self.tailgateRequired is not None and 'tailgateRequired' not in already_processed:
            already_processed.add('tailgateRequired')
            outfile.write(' tailgateRequired=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.tailgateRequired), input_name='tailgateRequired')), ))
        if self.residential is not None and 'residential' not in already_processed:
            already_processed.add('residential')
            outfile.write(' residential=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.residential), input_name='residential')), ))
        if self.instructions is not None and 'instructions' not in already_processed:
            already_processed.add('instructions')
            outfile.write(' instructions=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.instructions), input_name='instructions')), ))
        if self.address1 is not None and 'address1' not in already_processed:
            already_processed.add('address1')
            outfile.write(' address1=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.address1), input_name='address1')), ))
        if self.address2 is not None and 'address2' not in already_processed:
            already_processed.add('address2')
            outfile.write(' address2=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.address2), input_name='address2')), ))
        if self.city is not None and 'city' not in already_processed:
            already_processed.add('city')
            outfile.write(' city=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.city), input_name='city')), ))
        if self.state is not None and 'state' not in already_processed:
            already_processed.add('state')
            outfile.write(' state=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.state), input_name='state')), ))
        if self.country is not None and 'country' not in already_processed:
            already_processed.add('country')
            outfile.write(' country=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.country), input_name='country')), ))
        if self.zip is not None and 'zip' not in already_processed:
            already_processed.add('zip')
            outfile.write(' zip=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.zip), input_name='zip')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ToType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('company', node)
        if value is not None and 'company' not in already_processed:
            already_processed.add('company')
            self.company = value
        value = find_attr_value_('email', node)
        if value is not None and 'email' not in already_processed:
            already_processed.add('email')
            self.email = value
        value = find_attr_value_('notifyRecipient', node)
        if value is not None and 'notifyRecipient' not in already_processed:
            already_processed.add('notifyRecipient')
            self.notifyRecipient = value
        value = find_attr_value_('attention', node)
        if value is not None and 'attention' not in already_processed:
            already_processed.add('attention')
            self.attention = value
        value = find_attr_value_('phone', node)
        if value is not None and 'phone' not in already_processed:
            already_processed.add('phone')
            self.phone = value
        value = find_attr_value_('tailgateRequired', node)
        if value is not None and 'tailgateRequired' not in already_processed:
            already_processed.add('tailgateRequired')
            self.tailgateRequired = value
        value = find_attr_value_('residential', node)
        if value is not None and 'residential' not in already_processed:
            already_processed.add('residential')
            self.residential = value
        value = find_attr_value_('instructions', node)
        if value is not None and 'instructions' not in already_processed:
            already_processed.add('instructions')
            self.instructions = value
        value = find_attr_value_('address1', node)
        if value is not None and 'address1' not in already_processed:
            already_processed.add('address1')
            self.address1 = value
        value = find_attr_value_('address2', node)
        if value is not None and 'address2' not in already_processed:
            already_processed.add('address2')
            self.address2 = value
        value = find_attr_value_('city', node)
        if value is not None and 'city' not in already_processed:
            already_processed.add('city')
            self.city = value
        value = find_attr_value_('state', node)
        if value is not None and 'state' not in already_processed:
            already_processed.add('state')
            self.state = value
        value = find_attr_value_('country', node)
        if value is not None and 'country' not in already_processed:
            already_processed.add('country')
            self.country = value
        value = find_attr_value_('zip', node)
        if value is not None and 'zip' not in already_processed:
            already_processed.add('zip')
            self.zip = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class ToType


class ShipperType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, company=None, email=None, notifyRecipient=None, attention=None, phone=None, tailgateRequired=None, residential=None, instructions=None, address1=None, address2=None, city=None, state=None, country=None, zip=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.company = _cast(None, company)
        self.company_nsprefix_ = None
        self.email = _cast(None, email)
        self.email_nsprefix_ = None
        self.notifyRecipient = _cast(None, notifyRecipient)
        self.notifyRecipient_nsprefix_ = None
        self.attention = _cast(None, attention)
        self.attention_nsprefix_ = None
        self.phone = _cast(None, phone)
        self.phone_nsprefix_ = None
        self.tailgateRequired = _cast(None, tailgateRequired)
        self.tailgateRequired_nsprefix_ = None
        self.residential = _cast(None, residential)
        self.residential_nsprefix_ = None
        self.instructions = _cast(None, instructions)
        self.instructions_nsprefix_ = None
        self.address1 = _cast(None, address1)
        self.address1_nsprefix_ = None
        self.address2 = _cast(None, address2)
        self.address2_nsprefix_ = None
        self.city = _cast(None, city)
        self.city_nsprefix_ = None
        self.state = _cast(None, state)
        self.state_nsprefix_ = None
        self.country = _cast(None, country)
        self.country_nsprefix_ = None
        self.zip = _cast(None, zip)
        self.zip_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ShipperType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ShipperType.subclass:
            return ShipperType.subclass(*args_, **kwargs_)
        else:
            return ShipperType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_company(self):
        return self.company
    def set_company(self, company):
        self.company = company
    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email = email
    def get_notifyRecipient(self):
        return self.notifyRecipient
    def set_notifyRecipient(self, notifyRecipient):
        self.notifyRecipient = notifyRecipient
    def get_attention(self):
        return self.attention
    def set_attention(self, attention):
        self.attention = attention
    def get_phone(self):
        return self.phone
    def set_phone(self, phone):
        self.phone = phone
    def get_tailgateRequired(self):
        return self.tailgateRequired
    def set_tailgateRequired(self, tailgateRequired):
        self.tailgateRequired = tailgateRequired
    def get_residential(self):
        return self.residential
    def set_residential(self, residential):
        self.residential = residential
    def get_instructions(self):
        return self.instructions
    def set_instructions(self, instructions):
        self.instructions = instructions
    def get_address1(self):
        return self.address1
    def set_address1(self, address1):
        self.address1 = address1
    def get_address2(self):
        return self.address2
    def set_address2(self, address2):
        self.address2 = address2
    def get_city(self):
        return self.city
    def set_city(self, city):
        self.city = city
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
    def get_country(self):
        return self.country
    def set_country(self, country):
        self.country = country
    def get_zip(self):
        return self.zip
    def set_zip(self, zip):
        self.zip = zip
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipperType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ShipperType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ShipperType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ShipperType')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ShipperType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ShipperType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
        if self.company is not None and 'company' not in already_processed:
            already_processed.add('company')
            outfile.write(' company=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.company), input_name='company')), ))
        if self.email is not None and 'email' not in already_processed:
            already_processed.add('email')
            outfile.write(' email=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.email), input_name='email')), ))
        if self.notifyRecipient is not None and 'notifyRecipient' not in already_processed:
            already_processed.add('notifyRecipient')
            outfile.write(' notifyRecipient=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.notifyRecipient), input_name='notifyRecipient')), ))
        if self.attention is not None and 'attention' not in already_processed:
            already_processed.add('attention')
            outfile.write(' attention=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.attention), input_name='attention')), ))
        if self.phone is not None and 'phone' not in already_processed:
            already_processed.add('phone')
            outfile.write(' phone=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.phone), input_name='phone')), ))
        if self.tailgateRequired is not None and 'tailgateRequired' not in already_processed:
            already_processed.add('tailgateRequired')
            outfile.write(' tailgateRequired=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.tailgateRequired), input_name='tailgateRequired')), ))
        if self.residential is not None and 'residential' not in already_processed:
            already_processed.add('residential')
            outfile.write(' residential=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.residential), input_name='residential')), ))
        if self.instructions is not None and 'instructions' not in already_processed:
            already_processed.add('instructions')
            outfile.write(' instructions=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.instructions), input_name='instructions')), ))
        if self.address1 is not None and 'address1' not in already_processed:
            already_processed.add('address1')
            outfile.write(' address1=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.address1), input_name='address1')), ))
        if self.address2 is not None and 'address2' not in already_processed:
            already_processed.add('address2')
            outfile.write(' address2=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.address2), input_name='address2')), ))
        if self.city is not None and 'city' not in already_processed:
            already_processed.add('city')
            outfile.write(' city=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.city), input_name='city')), ))
        if self.state is not None and 'state' not in already_processed:
            already_processed.add('state')
            outfile.write(' state=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.state), input_name='state')), ))
        if self.country is not None and 'country' not in already_processed:
            already_processed.add('country')
            outfile.write(' country=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.country), input_name='country')), ))
        if self.zip is not None and 'zip' not in already_processed:
            already_processed.add('zip')
            outfile.write(' zip=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.zip), input_name='zip')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipperType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('company', node)
        if value is not None and 'company' not in already_processed:
            already_processed.add('company')
            self.company = value
        value = find_attr_value_('email', node)
        if value is not None and 'email' not in already_processed:
            already_processed.add('email')
            self.email = value
        value = find_attr_value_('notifyRecipient', node)
        if value is not None and 'notifyRecipient' not in already_processed:
            already_processed.add('notifyRecipient')
            self.notifyRecipient = value
        value = find_attr_value_('attention', node)
        if value is not None and 'attention' not in already_processed:
            already_processed.add('attention')
            self.attention = value
        value = find_attr_value_('phone', node)
        if value is not None and 'phone' not in already_processed:
            already_processed.add('phone')
            self.phone = value
        value = find_attr_value_('tailgateRequired', node)
        if value is not None and 'tailgateRequired' not in already_processed:
            already_processed.add('tailgateRequired')
            self.tailgateRequired = value
        value = find_attr_value_('residential', node)
        if value is not None and 'residential' not in already_processed:
            already_processed.add('residential')
            self.residential = value
        value = find_attr_value_('instructions', node)
        if value is not None and 'instructions' not in already_processed:
            already_processed.add('instructions')
            self.instructions = value
        value = find_attr_value_('address1', node)
        if value is not None and 'address1' not in already_processed:
            already_processed.add('address1')
            self.address1 = value
        value = find_attr_value_('address2', node)
        if value is not None and 'address2' not in already_processed:
            already_processed.add('address2')
            self.address2 = value
        value = find_attr_value_('city', node)
        if value is not None and 'city' not in already_processed:
            already_processed.add('city')
            self.city = value
        value = find_attr_value_('state', node)
        if value is not None and 'state' not in already_processed:
            already_processed.add('state')
            self.state = value
        value = find_attr_value_('country', node)
        if value is not None and 'country' not in already_processed:
            already_processed.add('country')
            self.country = value
        value = find_attr_value_('zip', node)
        if value is not None and 'zip' not in already_processed:
            already_processed.add('zip')
            self.zip = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class ShipperType


class CODType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, paymentType=None, CODReturnAddress=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.paymentType = _cast(None, paymentType)
        self.paymentType_nsprefix_ = None
        self.CODReturnAddress = CODReturnAddress
        self.CODReturnAddress_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CODType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CODType.subclass:
            return CODType.subclass(*args_, **kwargs_)
        else:
            return CODType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_CODReturnAddress(self):
        return self.CODReturnAddress
    def set_CODReturnAddress(self, CODReturnAddress):
        self.CODReturnAddress = CODReturnAddress
    def get_paymentType(self):
        return self.paymentType
    def set_paymentType(self, paymentType):
        self.paymentType = paymentType
    def _hasContent(self):
        if (
            self.CODReturnAddress is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CODType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CODType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CODType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CODType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CODType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CODType'):
        if self.paymentType is not None and 'paymentType' not in already_processed:
            already_processed.add('paymentType')
            outfile.write(' paymentType=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.paymentType), input_name='paymentType')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CODType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CODReturnAddress is not None:
            namespaceprefix_ = self.CODReturnAddress_nsprefix_ + ':' if (UseCapturedNS_ and self.CODReturnAddress_nsprefix_) else ''
            self.CODReturnAddress.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CODReturnAddress', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('paymentType', node)
        if value is not None and 'paymentType' not in already_processed:
            already_processed.add('paymentType')
            self.paymentType = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CODReturnAddress':
            obj_ = CODReturnAddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CODReturnAddress = obj_
            obj_.original_tagname_ = 'CODReturnAddress'
# end class CODType


class CODReturnAddressType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, codCompany=None, codName=None, codAddress1=None, codCity=None, codStateCode=None, codZip=None, codCountry=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.codCompany = _cast(None, codCompany)
        self.codCompany_nsprefix_ = None
        self.codName = _cast(None, codName)
        self.codName_nsprefix_ = None
        self.codAddress1 = _cast(None, codAddress1)
        self.codAddress1_nsprefix_ = None
        self.codCity = _cast(None, codCity)
        self.codCity_nsprefix_ = None
        self.codStateCode = _cast(None, codStateCode)
        self.codStateCode_nsprefix_ = None
        self.codZip = _cast(None, codZip)
        self.codZip_nsprefix_ = None
        self.codCountry = _cast(None, codCountry)
        self.codCountry_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CODReturnAddressType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CODReturnAddressType.subclass:
            return CODReturnAddressType.subclass(*args_, **kwargs_)
        else:
            return CODReturnAddressType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_codCompany(self):
        return self.codCompany
    def set_codCompany(self, codCompany):
        self.codCompany = codCompany
    def get_codName(self):
        return self.codName
    def set_codName(self, codName):
        self.codName = codName
    def get_codAddress1(self):
        return self.codAddress1
    def set_codAddress1(self, codAddress1):
        self.codAddress1 = codAddress1
    def get_codCity(self):
        return self.codCity
    def set_codCity(self, codCity):
        self.codCity = codCity
    def get_codStateCode(self):
        return self.codStateCode
    def set_codStateCode(self, codStateCode):
        self.codStateCode = codStateCode
    def get_codZip(self):
        return self.codZip
    def set_codZip(self, codZip):
        self.codZip = codZip
    def get_codCountry(self):
        return self.codCountry
    def set_codCountry(self, codCountry):
        self.codCountry = codCountry
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CODReturnAddressType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CODReturnAddressType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CODReturnAddressType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CODReturnAddressType')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CODReturnAddressType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CODReturnAddressType'):
        if self.codCompany is not None and 'codCompany' not in already_processed:
            already_processed.add('codCompany')
            outfile.write(' codCompany=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.codCompany), input_name='codCompany')), ))
        if self.codName is not None and 'codName' not in already_processed:
            already_processed.add('codName')
            outfile.write(' codName=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.codName), input_name='codName')), ))
        if self.codAddress1 is not None and 'codAddress1' not in already_processed:
            already_processed.add('codAddress1')
            outfile.write(' codAddress1=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.codAddress1), input_name='codAddress1')), ))
        if self.codCity is not None and 'codCity' not in already_processed:
            already_processed.add('codCity')
            outfile.write(' codCity=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.codCity), input_name='codCity')), ))
        if self.codStateCode is not None and 'codStateCode' not in already_processed:
            already_processed.add('codStateCode')
            outfile.write(' codStateCode=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.codStateCode), input_name='codStateCode')), ))
        if self.codZip is not None and 'codZip' not in already_processed:
            already_processed.add('codZip')
            outfile.write(' codZip=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.codZip), input_name='codZip')), ))
        if self.codCountry is not None and 'codCountry' not in already_processed:
            already_processed.add('codCountry')
            outfile.write(' codCountry=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.codCountry), input_name='codCountry')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CODReturnAddressType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('codCompany', node)
        if value is not None and 'codCompany' not in already_processed:
            already_processed.add('codCompany')
            self.codCompany = value
        value = find_attr_value_('codName', node)
        if value is not None and 'codName' not in already_processed:
            already_processed.add('codName')
            self.codName = value
        value = find_attr_value_('codAddress1', node)
        if value is not None and 'codAddress1' not in already_processed:
            already_processed.add('codAddress1')
            self.codAddress1 = value
        value = find_attr_value_('codCity', node)
        if value is not None and 'codCity' not in already_processed:
            already_processed.add('codCity')
            self.codCity = value
        value = find_attr_value_('codStateCode', node)
        if value is not None and 'codStateCode' not in already_processed:
            already_processed.add('codStateCode')
            self.codStateCode = value
        value = find_attr_value_('codZip', node)
        if value is not None and 'codZip' not in already_processed:
            already_processed.add('codZip')
            self.codZip = value
        value = find_attr_value_('codCountry', node)
        if value is not None and 'codCountry' not in already_processed:
            already_processed.add('codCountry')
            self.codCountry = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class CODReturnAddressType


class PackagesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, type_=None, Package=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None
        if Package is None:
            self.Package = []
        else:
            self.Package = Package
        self.Package_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PackagesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PackagesType.subclass:
            return PackagesType.subclass(*args_, **kwargs_)
        else:
            return PackagesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Package(self):
        return self.Package
    def set_Package(self, Package):
        self.Package = Package
    def add_Package(self, value):
        self.Package.append(value)
    def insert_Package_at(self, index, value):
        self.Package.insert(index, value)
    def replace_Package_at(self, index, value):
        self.Package[index] = value
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def _hasContent(self):
        if (
            self.Package
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PackagesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PackagesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PackagesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PackagesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PackagesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PackagesType'):
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PackagesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Package_ in self.Package:
            namespaceprefix_ = self.Package_nsprefix_ + ':' if (UseCapturedNS_ and self.Package_nsprefix_) else ''
            Package_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Package', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Package':
            obj_ = PackageType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Package.append(obj_)
            obj_.original_tagname_ = 'Package'
# end class PackagesType


class PackageType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, length=None, width=None, height=None, weight=None, weightOz=None, type_=None, freightClass=None, insuranceAmount=None, codAmount=None, description=None, nmfcCode=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.length = _cast(int, length)
        self.length_nsprefix_ = None
        self.width = _cast(int, width)
        self.width_nsprefix_ = None
        self.height = _cast(int, height)
        self.height_nsprefix_ = None
        self.weight = _cast(int, weight)
        self.weight_nsprefix_ = None
        self.weightOz = _cast(int, weightOz)
        self.weightOz_nsprefix_ = None
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None
        self.freightClass = _cast(None, freightClass)
        self.freightClass_nsprefix_ = None
        self.insuranceAmount = _cast(float, insuranceAmount)
        self.insuranceAmount_nsprefix_ = None
        self.codAmount = _cast(float, codAmount)
        self.codAmount_nsprefix_ = None
        self.description = _cast(None, description)
        self.description_nsprefix_ = None
        self.nmfcCode = _cast(int, nmfcCode)
        self.nmfcCode_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PackageType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PackageType.subclass:
            return PackageType.subclass(*args_, **kwargs_)
        else:
            return PackageType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_length(self):
        return self.length
    def set_length(self, length):
        self.length = length
    def get_width(self):
        return self.width
    def set_width(self, width):
        self.width = width
    def get_height(self):
        return self.height
    def set_height(self, height):
        self.height = height
    def get_weight(self):
        return self.weight
    def set_weight(self, weight):
        self.weight = weight
    def get_weightOz(self):
        return self.weightOz
    def set_weightOz(self, weightOz):
        self.weightOz = weightOz
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def get_freightClass(self):
        return self.freightClass
    def set_freightClass(self, freightClass):
        self.freightClass = freightClass
    def get_insuranceAmount(self):
        return self.insuranceAmount
    def set_insuranceAmount(self, insuranceAmount):
        self.insuranceAmount = insuranceAmount
    def get_codAmount(self):
        return self.codAmount
    def set_codAmount(self, codAmount):
        self.codAmount = codAmount
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def get_nmfcCode(self):
        return self.nmfcCode
    def set_nmfcCode(self, nmfcCode):
        self.nmfcCode = nmfcCode
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PackageType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PackageType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PackageType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PackageType')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PackageType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PackageType'):
        if self.length is not None and 'length' not in already_processed:
            already_processed.add('length')
            outfile.write(' length="%s"' % self.gds_format_integer(self.length, input_name='length'))
        if self.width is not None and 'width' not in already_processed:
            already_processed.add('width')
            outfile.write(' width="%s"' % self.gds_format_integer(self.width, input_name='width'))
        if self.height is not None and 'height' not in already_processed:
            already_processed.add('height')
            outfile.write(' height="%s"' % self.gds_format_integer(self.height, input_name='height'))
        if self.weight is not None and 'weight' not in already_processed:
            already_processed.add('weight')
            outfile.write(' weight="%s"' % self.gds_format_integer(self.weight, input_name='weight'))
        if self.weightOz is not None and 'weightOz' not in already_processed:
            already_processed.add('weightOz')
            outfile.write(' weightOz="%s"' % self.gds_format_integer(self.weightOz, input_name='weightOz'))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')), ))
        if self.freightClass is not None and 'freightClass' not in already_processed:
            already_processed.add('freightClass')
            outfile.write(' freightClass=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.freightClass), input_name='freightClass')), ))
        if self.insuranceAmount is not None and 'insuranceAmount' not in already_processed:
            already_processed.add('insuranceAmount')
            outfile.write(' insuranceAmount="%s"' % self.gds_format_float(self.insuranceAmount, input_name='insuranceAmount'))
        if self.codAmount is not None and 'codAmount' not in already_processed:
            already_processed.add('codAmount')
            outfile.write(' codAmount="%s"' % self.gds_format_float(self.codAmount, input_name='codAmount'))
        if self.description is not None and 'description' not in already_processed:
            already_processed.add('description')
            outfile.write(' description=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.description), input_name='description')), ))
        if self.nmfcCode is not None and 'nmfcCode' not in already_processed:
            already_processed.add('nmfcCode')
            outfile.write(' nmfcCode="%s"' % self.gds_format_integer(self.nmfcCode, input_name='nmfcCode'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PackageType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('length', node)
        if value is not None and 'length' not in already_processed:
            already_processed.add('length')
            self.length = self.gds_parse_integer(value, node, 'length')
        value = find_attr_value_('width', node)
        if value is not None and 'width' not in already_processed:
            already_processed.add('width')
            self.width = self.gds_parse_integer(value, node, 'width')
        value = find_attr_value_('height', node)
        if value is not None and 'height' not in already_processed:
            already_processed.add('height')
            self.height = self.gds_parse_integer(value, node, 'height')
        value = find_attr_value_('weight', node)
        if value is not None and 'weight' not in already_processed:
            already_processed.add('weight')
            self.weight = self.gds_parse_integer(value, node, 'weight')
        value = find_attr_value_('weightOz', node)
        if value is not None and 'weightOz' not in already_processed:
            already_processed.add('weightOz')
            self.weightOz = self.gds_parse_integer(value, node, 'weightOz')
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
        value = find_attr_value_('freightClass', node)
        if value is not None and 'freightClass' not in already_processed:
            already_processed.add('freightClass')
            self.freightClass = value
        value = find_attr_value_('insuranceAmount', node)
        if value is not None and 'insuranceAmount' not in already_processed:
            already_processed.add('insuranceAmount')
            value = self.gds_parse_float(value, node, 'insuranceAmount')
            self.insuranceAmount = value
        value = find_attr_value_('codAmount', node)
        if value is not None and 'codAmount' not in already_processed:
            already_processed.add('codAmount')
            value = self.gds_parse_float(value, node, 'codAmount')
            self.codAmount = value
        value = find_attr_value_('description', node)
        if value is not None and 'description' not in already_processed:
            already_processed.add('description')
            self.description = value
        value = find_attr_value_('nmfcCode', node)
        if value is not None and 'nmfcCode' not in already_processed:
            already_processed.add('nmfcCode')
            self.nmfcCode = self.gds_parse_integer(value, node, 'nmfcCode')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class PackageType


class PickupType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, contactName=None, phoneNumber=None, pickupDate=None, pickupTime=None, closingTime=None, location=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.contactName = _cast(None, contactName)
        self.contactName_nsprefix_ = None
        self.phoneNumber = _cast(None, phoneNumber)
        self.phoneNumber_nsprefix_ = None
        if isinstance(pickupDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(pickupDate, '%Y-%m-%d').date()
        else:
            initvalue_ = pickupDate
        self.pickupDate = initvalue_
        self.pickupTime = _cast(None, pickupTime)
        self.pickupTime_nsprefix_ = None
        self.closingTime = _cast(None, closingTime)
        self.closingTime_nsprefix_ = None
        self.location = _cast(None, location)
        self.location_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PickupType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PickupType.subclass:
            return PickupType.subclass(*args_, **kwargs_)
        else:
            return PickupType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_contactName(self):
        return self.contactName
    def set_contactName(self, contactName):
        self.contactName = contactName
    def get_phoneNumber(self):
        return self.phoneNumber
    def set_phoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber
    def get_pickupDate(self):
        return self.pickupDate
    def set_pickupDate(self, pickupDate):
        self.pickupDate = pickupDate
    def get_pickupTime(self):
        return self.pickupTime
    def set_pickupTime(self, pickupTime):
        self.pickupTime = pickupTime
    def get_closingTime(self):
        return self.closingTime
    def set_closingTime(self, closingTime):
        self.closingTime = closingTime
    def get_location(self):
        return self.location
    def set_location(self, location):
        self.location = location
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PickupType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PickupType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PickupType')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PickupType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PickupType'):
        if self.contactName is not None and 'contactName' not in already_processed:
            already_processed.add('contactName')
            outfile.write(' contactName=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.contactName), input_name='contactName')), ))
        if self.phoneNumber is not None and 'phoneNumber' not in already_processed:
            already_processed.add('phoneNumber')
            outfile.write(' phoneNumber=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.phoneNumber), input_name='phoneNumber')), ))
        if self.pickupDate is not None and 'pickupDate' not in already_processed:
            already_processed.add('pickupDate')
            outfile.write(' pickupDate="%s"' % self.gds_format_date(self.pickupDate, input_name='pickupDate'))
        if self.pickupTime is not None and 'pickupTime' not in already_processed:
            already_processed.add('pickupTime')
            outfile.write(' pickupTime=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.pickupTime), input_name='pickupTime')), ))
        if self.closingTime is not None and 'closingTime' not in already_processed:
            already_processed.add('closingTime')
            outfile.write(' closingTime=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.closingTime), input_name='closingTime')), ))
        if self.location is not None and 'location' not in already_processed:
            already_processed.add('location')
            outfile.write(' location=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.location), input_name='location')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('contactName', node)
        if value is not None and 'contactName' not in already_processed:
            already_processed.add('contactName')
            self.contactName = value
        value = find_attr_value_('phoneNumber', node)
        if value is not None and 'phoneNumber' not in already_processed:
            already_processed.add('phoneNumber')
            self.phoneNumber = value
        value = find_attr_value_('pickupDate', node)
        if value is not None and 'pickupDate' not in already_processed:
            already_processed.add('pickupDate')
            try:
                self.pickupDate = self.gds_parse_date(value)
            except ValueError as exp:
                raise ValueError('Bad date attribute (pickupDate): %s' % exp)
        value = find_attr_value_('pickupTime', node)
        if value is not None and 'pickupTime' not in already_processed:
            already_processed.add('pickupTime')
            self.pickupTime = value
        value = find_attr_value_('closingTime', node)
        if value is not None and 'closingTime' not in already_processed:
            already_processed.add('closingTime')
            self.closingTime = value
        value = find_attr_value_('location', node)
        if value is not None and 'location' not in already_processed:
            already_processed.add('location')
            self.location = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class PickupType


class PaymentType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, type_=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PaymentType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PaymentType.subclass:
            return PaymentType.subclass(*args_, **kwargs_)
        else:
            return PaymentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PaymentType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PaymentType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PaymentType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PaymentType')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PaymentType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PaymentType'):
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PaymentType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class PaymentType


class ReferenceType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, code=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.code = _cast(None, code)
        self.code_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ReferenceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ReferenceType.subclass:
            return ReferenceType.subclass(*args_, **kwargs_)
        else:
            return ReferenceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_code(self):
        return self.code
    def set_code(self, code):
        self.code = code
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ReferenceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ReferenceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ReferenceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ReferenceType')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ReferenceType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ReferenceType'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.code is not None and 'code' not in already_processed:
            already_processed.add('code')
            outfile.write(' code=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.code), input_name='code')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ReferenceType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
        value = find_attr_value_('code', node)
        if value is not None and 'code' not in already_processed:
            already_processed.add('code')
            self.code = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class ReferenceType


class CustomsInvoiceType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Currency=None, brokerName=None, contactCompany=None, shipperTaxID=None, receiverTaxID=None, contactName=None, contactPhone=None, BillTo=None, Contact=None, Item=None, DutiesTaxes=None, InBondManifest=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Currency = _cast(None, Currency)
        self.Currency_nsprefix_ = None
        self.brokerName = _cast(None, brokerName)
        self.brokerName_nsprefix_ = None
        self.contactCompany = _cast(None, contactCompany)
        self.contactCompany_nsprefix_ = None
        self.shipperTaxID = _cast(None, shipperTaxID)
        self.shipperTaxID_nsprefix_ = None
        self.receiverTaxID = _cast(None, receiverTaxID)
        self.receiverTaxID_nsprefix_ = None
        self.contactName = _cast(None, contactName)
        self.contactName_nsprefix_ = None
        self.contactPhone = _cast(None, contactPhone)
        self.contactPhone_nsprefix_ = None
        self.BillTo = BillTo
        self.BillTo_nsprefix_ = None
        self.Contact = Contact
        self.Contact_nsprefix_ = None
        self.Item = Item
        self.Item_nsprefix_ = None
        self.DutiesTaxes = DutiesTaxes
        self.DutiesTaxes_nsprefix_ = None
        self.InBondManifest = InBondManifest
        self.InBondManifest_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CustomsInvoiceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CustomsInvoiceType.subclass:
            return CustomsInvoiceType.subclass(*args_, **kwargs_)
        else:
            return CustomsInvoiceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_BillTo(self):
        return self.BillTo
    def set_BillTo(self, BillTo):
        self.BillTo = BillTo
    def get_Contact(self):
        return self.Contact
    def set_Contact(self, Contact):
        self.Contact = Contact
    def get_Item(self):
        return self.Item
    def set_Item(self, Item):
        self.Item = Item
    def get_DutiesTaxes(self):
        return self.DutiesTaxes
    def set_DutiesTaxes(self, DutiesTaxes):
        self.DutiesTaxes = DutiesTaxes
    def get_InBondManifest(self):
        return self.InBondManifest
    def set_InBondManifest(self, InBondManifest):
        self.InBondManifest = InBondManifest
    def get_Currency(self):
        return self.Currency
    def set_Currency(self, Currency):
        self.Currency = Currency
    def get_brokerName(self):
        return self.brokerName
    def set_brokerName(self, brokerName):
        self.brokerName = brokerName
    def get_contactCompany(self):
        return self.contactCompany
    def set_contactCompany(self, contactCompany):
        self.contactCompany = contactCompany
    def get_shipperTaxID(self):
        return self.shipperTaxID
    def set_shipperTaxID(self, shipperTaxID):
        self.shipperTaxID = shipperTaxID
    def get_receiverTaxID(self):
        return self.receiverTaxID
    def set_receiverTaxID(self, receiverTaxID):
        self.receiverTaxID = receiverTaxID
    def get_contactName(self):
        return self.contactName
    def set_contactName(self, contactName):
        self.contactName = contactName
    def get_contactPhone(self):
        return self.contactPhone
    def set_contactPhone(self, contactPhone):
        self.contactPhone = contactPhone
    def _hasContent(self):
        if (
            self.BillTo is not None or
            self.Contact is not None or
            self.Item is not None or
            self.DutiesTaxes is not None or
            self.InBondManifest is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CustomsInvoiceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CustomsInvoiceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CustomsInvoiceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CustomsInvoiceType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CustomsInvoiceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CustomsInvoiceType'):
        if self.Currency is not None and 'Currency' not in already_processed:
            already_processed.add('Currency')
            outfile.write(' Currency=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Currency), input_name='Currency')), ))
        if self.brokerName is not None and 'brokerName' not in already_processed:
            already_processed.add('brokerName')
            outfile.write(' brokerName=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.brokerName), input_name='brokerName')), ))
        if self.contactCompany is not None and 'contactCompany' not in already_processed:
            already_processed.add('contactCompany')
            outfile.write(' contactCompany=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.contactCompany), input_name='contactCompany')), ))
        if self.shipperTaxID is not None and 'shipperTaxID' not in already_processed:
            already_processed.add('shipperTaxID')
            outfile.write(' shipperTaxID=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.shipperTaxID), input_name='shipperTaxID')), ))
        if self.receiverTaxID is not None and 'receiverTaxID' not in already_processed:
            already_processed.add('receiverTaxID')
            outfile.write(' receiverTaxID=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.receiverTaxID), input_name='receiverTaxID')), ))
        if self.contactName is not None and 'contactName' not in already_processed:
            already_processed.add('contactName')
            outfile.write(' contactName=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.contactName), input_name='contactName')), ))
        if self.contactPhone is not None and 'contactPhone' not in already_processed:
            already_processed.add('contactPhone')
            outfile.write(' contactPhone=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.contactPhone), input_name='contactPhone')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CustomsInvoiceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.BillTo is not None:
            namespaceprefix_ = self.BillTo_nsprefix_ + ':' if (UseCapturedNS_ and self.BillTo_nsprefix_) else ''
            self.BillTo.export(outfile, level, namespaceprefix_, namespacedef_='', name_='BillTo', pretty_print=pretty_print)
        if self.Contact is not None:
            namespaceprefix_ = self.Contact_nsprefix_ + ':' if (UseCapturedNS_ and self.Contact_nsprefix_) else ''
            self.Contact.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Contact', pretty_print=pretty_print)
        if self.Item is not None:
            namespaceprefix_ = self.Item_nsprefix_ + ':' if (UseCapturedNS_ and self.Item_nsprefix_) else ''
            self.Item.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Item', pretty_print=pretty_print)
        if self.DutiesTaxes is not None:
            namespaceprefix_ = self.DutiesTaxes_nsprefix_ + ':' if (UseCapturedNS_ and self.DutiesTaxes_nsprefix_) else ''
            self.DutiesTaxes.export(outfile, level, namespaceprefix_, namespacedef_='', name_='DutiesTaxes', pretty_print=pretty_print)
        if self.InBondManifest is not None:
            namespaceprefix_ = self.InBondManifest_nsprefix_ + ':' if (UseCapturedNS_ and self.InBondManifest_nsprefix_) else ''
            self.InBondManifest.export(outfile, level, namespaceprefix_, namespacedef_='', name_='InBondManifest', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Currency', node)
        if value is not None and 'Currency' not in already_processed:
            already_processed.add('Currency')
            self.Currency = value
        value = find_attr_value_('brokerName', node)
        if value is not None and 'brokerName' not in already_processed:
            already_processed.add('brokerName')
            self.brokerName = value
        value = find_attr_value_('contactCompany', node)
        if value is not None and 'contactCompany' not in already_processed:
            already_processed.add('contactCompany')
            self.contactCompany = value
        value = find_attr_value_('shipperTaxID', node)
        if value is not None and 'shipperTaxID' not in already_processed:
            already_processed.add('shipperTaxID')
            self.shipperTaxID = value
        value = find_attr_value_('receiverTaxID', node)
        if value is not None and 'receiverTaxID' not in already_processed:
            already_processed.add('receiverTaxID')
            self.receiverTaxID = value
        value = find_attr_value_('contactName', node)
        if value is not None and 'contactName' not in already_processed:
            already_processed.add('contactName')
            self.contactName = value
        value = find_attr_value_('contactPhone', node)
        if value is not None and 'contactPhone' not in already_processed:
            already_processed.add('contactPhone')
            self.contactPhone = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'BillTo':
            obj_ = BillToType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BillTo = obj_
            obj_.original_tagname_ = 'BillTo'
        elif nodeName_ == 'Contact':
            obj_ = ContactType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Contact = obj_
            obj_.original_tagname_ = 'Contact'
        elif nodeName_ == 'Item':
            obj_ = ItemType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Item = obj_
            obj_.original_tagname_ = 'Item'
        elif nodeName_ == 'DutiesTaxes':
            obj_ = DutiesTaxesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DutiesTaxes = obj_
            obj_.original_tagname_ = 'DutiesTaxes'
        elif nodeName_ == 'InBondManifest':
            obj_ = InBondManifestType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.InBondManifest = obj_
            obj_.original_tagname_ = 'InBondManifest'
# end class CustomsInvoiceType


class BillToType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, company=None, name=None, address1=None, city=None, state=None, zip=None, country=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.company = _cast(None, company)
        self.company_nsprefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.address1 = _cast(None, address1)
        self.address1_nsprefix_ = None
        self.city = _cast(None, city)
        self.city_nsprefix_ = None
        self.state = _cast(None, state)
        self.state_nsprefix_ = None
        self.zip = _cast(None, zip)
        self.zip_nsprefix_ = None
        self.country = _cast(None, country)
        self.country_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, BillToType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if BillToType.subclass:
            return BillToType.subclass(*args_, **kwargs_)
        else:
            return BillToType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_company(self):
        return self.company
    def set_company(self, company):
        self.company = company
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_address1(self):
        return self.address1
    def set_address1(self, address1):
        self.address1 = address1
    def get_city(self):
        return self.city
    def set_city(self, city):
        self.city = city
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
    def get_zip(self):
        return self.zip
    def set_zip(self, zip):
        self.zip = zip
    def get_country(self):
        return self.country
    def set_country(self, country):
        self.country = country
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='BillToType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('BillToType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'BillToType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='BillToType')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='BillToType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='BillToType'):
        if self.company is not None and 'company' not in already_processed:
            already_processed.add('company')
            outfile.write(' company=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.company), input_name='company')), ))
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.address1 is not None and 'address1' not in already_processed:
            already_processed.add('address1')
            outfile.write(' address1=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.address1), input_name='address1')), ))
        if self.city is not None and 'city' not in already_processed:
            already_processed.add('city')
            outfile.write(' city=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.city), input_name='city')), ))
        if self.state is not None and 'state' not in already_processed:
            already_processed.add('state')
            outfile.write(' state=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.state), input_name='state')), ))
        if self.zip is not None and 'zip' not in already_processed:
            already_processed.add('zip')
            outfile.write(' zip=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.zip), input_name='zip')), ))
        if self.country is not None and 'country' not in already_processed:
            already_processed.add('country')
            outfile.write(' country=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.country), input_name='country')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='BillToType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('company', node)
        if value is not None and 'company' not in already_processed:
            already_processed.add('company')
            self.company = value
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
        value = find_attr_value_('address1', node)
        if value is not None and 'address1' not in already_processed:
            already_processed.add('address1')
            self.address1 = value
        value = find_attr_value_('city', node)
        if value is not None and 'city' not in already_processed:
            already_processed.add('city')
            self.city = value
        value = find_attr_value_('state', node)
        if value is not None and 'state' not in already_processed:
            already_processed.add('state')
            self.state = value
        value = find_attr_value_('zip', node)
        if value is not None and 'zip' not in already_processed:
            already_processed.add('zip')
            self.zip = value
        value = find_attr_value_('country', node)
        if value is not None and 'country' not in already_processed:
            already_processed.add('country')
            self.country = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class BillToType


class ContactType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, phone=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.phone = _cast(None, phone)
        self.phone_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ContactType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ContactType.subclass:
            return ContactType.subclass(*args_, **kwargs_)
        else:
            return ContactType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_phone(self):
        return self.phone
    def set_phone(self, phone):
        self.phone = phone
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ContactType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ContactType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ContactType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ContactType')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ContactType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ContactType'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.phone is not None and 'phone' not in already_processed:
            already_processed.add('phone')
            outfile.write(' phone=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.phone), input_name='phone')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ContactType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
        value = find_attr_value_('phone', node)
        if value is not None and 'phone' not in already_processed:
            already_processed.add('phone')
            self.phone = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class ContactType


class ItemType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, code=None, description=None, originCountry=None, quantity=None, unitPrice=None, skuCode=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.code = _cast(None, code)
        self.code_nsprefix_ = None
        self.description = _cast(None, description)
        self.description_nsprefix_ = None
        self.originCountry = _cast(None, originCountry)
        self.originCountry_nsprefix_ = None
        self.quantity = _cast(int, quantity)
        self.quantity_nsprefix_ = None
        self.unitPrice = _cast(float, unitPrice)
        self.unitPrice_nsprefix_ = None
        self.skuCode = _cast(None, skuCode)
        self.skuCode_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ItemType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ItemType.subclass:
            return ItemType.subclass(*args_, **kwargs_)
        else:
            return ItemType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_code(self):
        return self.code
    def set_code(self, code):
        self.code = code
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def get_originCountry(self):
        return self.originCountry
    def set_originCountry(self, originCountry):
        self.originCountry = originCountry
    def get_quantity(self):
        return self.quantity
    def set_quantity(self, quantity):
        self.quantity = quantity
    def get_unitPrice(self):
        return self.unitPrice
    def set_unitPrice(self, unitPrice):
        self.unitPrice = unitPrice
    def get_skuCode(self):
        return self.skuCode
    def set_skuCode(self, skuCode):
        self.skuCode = skuCode
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ItemType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ItemType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ItemType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ItemType')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ItemType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ItemType'):
        if self.code is not None and 'code' not in already_processed:
            already_processed.add('code')
            outfile.write(' code=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.code), input_name='code')), ))
        if self.description is not None and 'description' not in already_processed:
            already_processed.add('description')
            outfile.write(' description=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.description), input_name='description')), ))
        if self.originCountry is not None and 'originCountry' not in already_processed:
            already_processed.add('originCountry')
            outfile.write(' originCountry=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.originCountry), input_name='originCountry')), ))
        if self.quantity is not None and 'quantity' not in already_processed:
            already_processed.add('quantity')
            outfile.write(' quantity="%s"' % self.gds_format_integer(self.quantity, input_name='quantity'))
        if self.unitPrice is not None and 'unitPrice' not in already_processed:
            already_processed.add('unitPrice')
            outfile.write(' unitPrice="%s"' % self.gds_format_float(self.unitPrice, input_name='unitPrice'))
        if self.skuCode is not None and 'skuCode' not in already_processed:
            already_processed.add('skuCode')
            outfile.write(' skuCode=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.skuCode), input_name='skuCode')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ItemType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('code', node)
        if value is not None and 'code' not in already_processed:
            already_processed.add('code')
            self.code = value
        value = find_attr_value_('description', node)
        if value is not None and 'description' not in already_processed:
            already_processed.add('description')
            self.description = value
        value = find_attr_value_('originCountry', node)
        if value is not None and 'originCountry' not in already_processed:
            already_processed.add('originCountry')
            self.originCountry = value
        value = find_attr_value_('quantity', node)
        if value is not None and 'quantity' not in already_processed:
            already_processed.add('quantity')
            self.quantity = self.gds_parse_integer(value, node, 'quantity')
        value = find_attr_value_('unitPrice', node)
        if value is not None and 'unitPrice' not in already_processed:
            already_processed.add('unitPrice')
            value = self.gds_parse_float(value, node, 'unitPrice')
            self.unitPrice = value
        value = find_attr_value_('skuCode', node)
        if value is not None and 'skuCode' not in already_processed:
            already_processed.add('skuCode')
            self.skuCode = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class ItemType


class DutiesTaxesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, consigneeAccount=None, sedNumber=None, dutiable=None, billTo=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.consigneeAccount = _cast(None, consigneeAccount)
        self.consigneeAccount_nsprefix_ = None
        self.sedNumber = _cast(None, sedNumber)
        self.sedNumber_nsprefix_ = None
        self.dutiable = _cast(None, dutiable)
        self.dutiable_nsprefix_ = None
        self.billTo = _cast(None, billTo)
        self.billTo_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DutiesTaxesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DutiesTaxesType.subclass:
            return DutiesTaxesType.subclass(*args_, **kwargs_)
        else:
            return DutiesTaxesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_consigneeAccount(self):
        return self.consigneeAccount
    def set_consigneeAccount(self, consigneeAccount):
        self.consigneeAccount = consigneeAccount
    def get_sedNumber(self):
        return self.sedNumber
    def set_sedNumber(self, sedNumber):
        self.sedNumber = sedNumber
    def get_dutiable(self):
        return self.dutiable
    def set_dutiable(self, dutiable):
        self.dutiable = dutiable
    def get_billTo(self):
        return self.billTo
    def set_billTo(self, billTo):
        self.billTo = billTo
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DutiesTaxesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DutiesTaxesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DutiesTaxesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DutiesTaxesType')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DutiesTaxesType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DutiesTaxesType'):
        if self.consigneeAccount is not None and 'consigneeAccount' not in already_processed:
            already_processed.add('consigneeAccount')
            outfile.write(' consigneeAccount=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.consigneeAccount), input_name='consigneeAccount')), ))
        if self.sedNumber is not None and 'sedNumber' not in already_processed:
            already_processed.add('sedNumber')
            outfile.write(' sedNumber=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.sedNumber), input_name='sedNumber')), ))
        if self.dutiable is not None and 'dutiable' not in already_processed:
            already_processed.add('dutiable')
            outfile.write(' dutiable=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.dutiable), input_name='dutiable')), ))
        if self.billTo is not None and 'billTo' not in already_processed:
            already_processed.add('billTo')
            outfile.write(' billTo=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.billTo), input_name='billTo')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DutiesTaxesType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('consigneeAccount', node)
        if value is not None and 'consigneeAccount' not in already_processed:
            already_processed.add('consigneeAccount')
            self.consigneeAccount = value
        value = find_attr_value_('sedNumber', node)
        if value is not None and 'sedNumber' not in already_processed:
            already_processed.add('sedNumber')
            self.sedNumber = value
        value = find_attr_value_('dutiable', node)
        if value is not None and 'dutiable' not in already_processed:
            already_processed.add('dutiable')
            self.dutiable = value
        value = find_attr_value_('billTo', node)
        if value is not None and 'billTo' not in already_processed:
            already_processed.add('billTo')
            self.billTo = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class DutiesTaxesType


class InBondManifestType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, locationOfGoods=None, nameOfCarrier=None, vehicleIdentification=None, customsClearedBy=None, handlingInfo=None, previousCargoControlNum=None, weight=None, weightUOM=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.locationOfGoods = _cast(None, locationOfGoods)
        self.locationOfGoods_nsprefix_ = None
        self.nameOfCarrier = _cast(None, nameOfCarrier)
        self.nameOfCarrier_nsprefix_ = None
        self.vehicleIdentification = _cast(int, vehicleIdentification)
        self.vehicleIdentification_nsprefix_ = None
        self.customsClearedBy = _cast(None, customsClearedBy)
        self.customsClearedBy_nsprefix_ = None
        self.handlingInfo = _cast(None, handlingInfo)
        self.handlingInfo_nsprefix_ = None
        self.previousCargoControlNum = _cast(int, previousCargoControlNum)
        self.previousCargoControlNum_nsprefix_ = None
        self.weight = _cast(float, weight)
        self.weight_nsprefix_ = None
        self.weightUOM = _cast(None, weightUOM)
        self.weightUOM_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InBondManifestType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InBondManifestType.subclass:
            return InBondManifestType.subclass(*args_, **kwargs_)
        else:
            return InBondManifestType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_locationOfGoods(self):
        return self.locationOfGoods
    def set_locationOfGoods(self, locationOfGoods):
        self.locationOfGoods = locationOfGoods
    def get_nameOfCarrier(self):
        return self.nameOfCarrier
    def set_nameOfCarrier(self, nameOfCarrier):
        self.nameOfCarrier = nameOfCarrier
    def get_vehicleIdentification(self):
        return self.vehicleIdentification
    def set_vehicleIdentification(self, vehicleIdentification):
        self.vehicleIdentification = vehicleIdentification
    def get_customsClearedBy(self):
        return self.customsClearedBy
    def set_customsClearedBy(self, customsClearedBy):
        self.customsClearedBy = customsClearedBy
    def get_handlingInfo(self):
        return self.handlingInfo
    def set_handlingInfo(self, handlingInfo):
        self.handlingInfo = handlingInfo
    def get_previousCargoControlNum(self):
        return self.previousCargoControlNum
    def set_previousCargoControlNum(self, previousCargoControlNum):
        self.previousCargoControlNum = previousCargoControlNum
    def get_weight(self):
        return self.weight
    def set_weight(self, weight):
        self.weight = weight
    def get_weightUOM(self):
        return self.weightUOM
    def set_weightUOM(self, weightUOM):
        self.weightUOM = weightUOM
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='InBondManifestType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InBondManifestType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InBondManifestType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InBondManifestType')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InBondManifestType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='InBondManifestType'):
        if self.locationOfGoods is not None and 'locationOfGoods' not in already_processed:
            already_processed.add('locationOfGoods')
            outfile.write(' locationOfGoods=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.locationOfGoods), input_name='locationOfGoods')), ))
        if self.nameOfCarrier is not None and 'nameOfCarrier' not in already_processed:
            already_processed.add('nameOfCarrier')
            outfile.write(' nameOfCarrier=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.nameOfCarrier), input_name='nameOfCarrier')), ))
        if self.vehicleIdentification is not None and 'vehicleIdentification' not in already_processed:
            already_processed.add('vehicleIdentification')
            outfile.write(' vehicleIdentification="%s"' % self.gds_format_integer(self.vehicleIdentification, input_name='vehicleIdentification'))
        if self.customsClearedBy is not None and 'customsClearedBy' not in already_processed:
            already_processed.add('customsClearedBy')
            outfile.write(' customsClearedBy=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.customsClearedBy), input_name='customsClearedBy')), ))
        if self.handlingInfo is not None and 'handlingInfo' not in already_processed:
            already_processed.add('handlingInfo')
            outfile.write(' handlingInfo=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.handlingInfo), input_name='handlingInfo')), ))
        if self.previousCargoControlNum is not None and 'previousCargoControlNum' not in already_processed:
            already_processed.add('previousCargoControlNum')
            outfile.write(' previousCargoControlNum="%s"' % self.gds_format_integer(self.previousCargoControlNum, input_name='previousCargoControlNum'))
        if self.weight is not None and 'weight' not in already_processed:
            already_processed.add('weight')
            outfile.write(' weight="%s"' % self.gds_format_float(self.weight, input_name='weight'))
        if self.weightUOM is not None and 'weightUOM' not in already_processed:
            already_processed.add('weightUOM')
            outfile.write(' weightUOM=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.weightUOM), input_name='weightUOM')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='InBondManifestType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('locationOfGoods', node)
        if value is not None and 'locationOfGoods' not in already_processed:
            already_processed.add('locationOfGoods')
            self.locationOfGoods = value
        value = find_attr_value_('nameOfCarrier', node)
        if value is not None and 'nameOfCarrier' not in already_processed:
            already_processed.add('nameOfCarrier')
            self.nameOfCarrier = value
        value = find_attr_value_('vehicleIdentification', node)
        if value is not None and 'vehicleIdentification' not in already_processed:
            already_processed.add('vehicleIdentification')
            self.vehicleIdentification = self.gds_parse_integer(value, node, 'vehicleIdentification')
        value = find_attr_value_('customsClearedBy', node)
        if value is not None and 'customsClearedBy' not in already_processed:
            already_processed.add('customsClearedBy')
            self.customsClearedBy = value
        value = find_attr_value_('handlingInfo', node)
        if value is not None and 'handlingInfo' not in already_processed:
            already_processed.add('handlingInfo')
            self.handlingInfo = value
        value = find_attr_value_('previousCargoControlNum', node)
        if value is not None and 'previousCargoControlNum' not in already_processed:
            already_processed.add('previousCargoControlNum')
            self.previousCargoControlNum = self.gds_parse_integer(value, node, 'previousCargoControlNum')
        value = find_attr_value_('weight', node)
        if value is not None and 'weight' not in already_processed:
            already_processed.add('weight')
            value = self.gds_parse_float(value, node, 'weight')
            self.weight = value
        value = find_attr_value_('weightUOM', node)
        if value is not None and 'weightUOM' not in already_processed:
            already_processed.add('weightUOM')
            self.weightUOM = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class InBondManifestType


GDSClassesMapping = {
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'EShipper'
        rootClass = EShipper
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_=namespacedefs,
            pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'EShipper'
        rootClass = EShipper
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if mapping is None:
        mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping, nsmap_=nsmap)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(str(content))
        sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'EShipper'
        rootClass = EShipper
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'EShipper'
        rootClass = EShipper
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from shipping_request import *\n\n')
        sys.stdout.write('import shipping_request as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
}

#
# Mapping of namespaces to types defined in them
# and the file in which each is defined.
# simpleTypes are marked "ST" and complexTypes "CT".
NamespaceToDefMappings_ = {'http://www.eshipper.net/XMLSchema': []}

__all__ = [
    "BillToType",
    "CODReturnAddressType",
    "CODType",
    "ContactType",
    "CustomsInvoiceType",
    "DutiesTaxesType",
    "EShipper",
    "FromType",
    "InBondManifestType",
    "ItemType",
    "PackageType",
    "PackagesType",
    "PaymentType",
    "PickupType",
    "ReferenceType",
    "ShipperType",
    "ShippingRequestType",
    "ToType"
]
