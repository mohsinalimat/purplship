#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Sat May 29 15:47:03 2021 by generateDS.py version 2.38.6.
# Python 3.8.6 (v3.8.6:db455296be, Sep 23 2020, 13:31:39)  [Clang 6.0 (clang-600.0.57)]
#
# Command line options:
#   ('--no-namespace-defs', '')
#   ('-o', './usps_lib/evs_priority_mail_intl_response.py')
#
# Command line arguments:
#   ./schemas/eVSPriorityMailIntlResponse.xsd
#
# Command line:
#   /Users/danielkobina/Workspace/project/karrio-carriers/.venv/karrio-carriers/bin/generateDS --no-namespace-defs -o "./usps_lib/evs_priority_mail_intl_response.py" ./schemas/eVSPriorityMailIntlResponse.xsd
#
# Current working directory (os.getcwd()):
#   usps
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
# "xsi:type" attribute value.  See the exportAttributes method of
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
    
    class GeneratedsSuper(object):
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


class eVSPriorityMailIntlResponse(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Postage=None, TotalValue=None, SDRValue=None, BarcodeNumber=None, LabelImage=None, Page2Image=None, Page3Image=None, Page4Image=None, Page5Image=None, Page6Image=None, Prohibitions=None, Restrictions=None, Observations=None, Regulations=None, AdditionalRestrictions=None, ParcelIndemnityCoverage=None, ExtraServices=None, RemainingBarcodes=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Postage = Postage
        self.Postage_nsprefix_ = None
        self.TotalValue = TotalValue
        self.TotalValue_nsprefix_ = None
        self.SDRValue = SDRValue
        self.SDRValue_nsprefix_ = None
        self.BarcodeNumber = BarcodeNumber
        self.BarcodeNumber_nsprefix_ = None
        self.LabelImage = LabelImage
        self.LabelImage_nsprefix_ = None
        self.Page2Image = Page2Image
        self.Page2Image_nsprefix_ = None
        self.Page3Image = Page3Image
        self.Page3Image_nsprefix_ = None
        self.Page4Image = Page4Image
        self.Page4Image_nsprefix_ = None
        self.Page5Image = Page5Image
        self.Page5Image_nsprefix_ = None
        self.Page6Image = Page6Image
        self.Page6Image_nsprefix_ = None
        self.Prohibitions = Prohibitions
        self.Prohibitions_nsprefix_ = None
        self.Restrictions = Restrictions
        self.Restrictions_nsprefix_ = None
        self.Observations = Observations
        self.Observations_nsprefix_ = None
        self.Regulations = Regulations
        self.Regulations_nsprefix_ = None
        self.AdditionalRestrictions = AdditionalRestrictions
        self.AdditionalRestrictions_nsprefix_ = None
        self.ParcelIndemnityCoverage = ParcelIndemnityCoverage
        self.ParcelIndemnityCoverage_nsprefix_ = None
        self.ExtraServices = ExtraServices
        self.ExtraServices_nsprefix_ = None
        self.RemainingBarcodes = RemainingBarcodes
        self.RemainingBarcodes_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, eVSPriorityMailIntlResponse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if eVSPriorityMailIntlResponse.subclass:
            return eVSPriorityMailIntlResponse.subclass(*args_, **kwargs_)
        else:
            return eVSPriorityMailIntlResponse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Postage(self):
        return self.Postage
    def set_Postage(self, Postage):
        self.Postage = Postage
    def get_TotalValue(self):
        return self.TotalValue
    def set_TotalValue(self, TotalValue):
        self.TotalValue = TotalValue
    def get_SDRValue(self):
        return self.SDRValue
    def set_SDRValue(self, SDRValue):
        self.SDRValue = SDRValue
    def get_BarcodeNumber(self):
        return self.BarcodeNumber
    def set_BarcodeNumber(self, BarcodeNumber):
        self.BarcodeNumber = BarcodeNumber
    def get_LabelImage(self):
        return self.LabelImage
    def set_LabelImage(self, LabelImage):
        self.LabelImage = LabelImage
    def get_Page2Image(self):
        return self.Page2Image
    def set_Page2Image(self, Page2Image):
        self.Page2Image = Page2Image
    def get_Page3Image(self):
        return self.Page3Image
    def set_Page3Image(self, Page3Image):
        self.Page3Image = Page3Image
    def get_Page4Image(self):
        return self.Page4Image
    def set_Page4Image(self, Page4Image):
        self.Page4Image = Page4Image
    def get_Page5Image(self):
        return self.Page5Image
    def set_Page5Image(self, Page5Image):
        self.Page5Image = Page5Image
    def get_Page6Image(self):
        return self.Page6Image
    def set_Page6Image(self, Page6Image):
        self.Page6Image = Page6Image
    def get_Prohibitions(self):
        return self.Prohibitions
    def set_Prohibitions(self, Prohibitions):
        self.Prohibitions = Prohibitions
    def get_Restrictions(self):
        return self.Restrictions
    def set_Restrictions(self, Restrictions):
        self.Restrictions = Restrictions
    def get_Observations(self):
        return self.Observations
    def set_Observations(self, Observations):
        self.Observations = Observations
    def get_Regulations(self):
        return self.Regulations
    def set_Regulations(self, Regulations):
        self.Regulations = Regulations
    def get_AdditionalRestrictions(self):
        return self.AdditionalRestrictions
    def set_AdditionalRestrictions(self, AdditionalRestrictions):
        self.AdditionalRestrictions = AdditionalRestrictions
    def get_ParcelIndemnityCoverage(self):
        return self.ParcelIndemnityCoverage
    def set_ParcelIndemnityCoverage(self, ParcelIndemnityCoverage):
        self.ParcelIndemnityCoverage = ParcelIndemnityCoverage
    def get_ExtraServices(self):
        return self.ExtraServices
    def set_ExtraServices(self, ExtraServices):
        self.ExtraServices = ExtraServices
    def get_RemainingBarcodes(self):
        return self.RemainingBarcodes
    def set_RemainingBarcodes(self, RemainingBarcodes):
        self.RemainingBarcodes = RemainingBarcodes
    def hasContent_(self):
        if (
            self.Postage is not None or
            self.TotalValue is not None or
            self.SDRValue is not None or
            self.BarcodeNumber is not None or
            self.LabelImage is not None or
            self.Page2Image is not None or
            self.Page3Image is not None or
            self.Page4Image is not None or
            self.Page5Image is not None or
            self.Page6Image is not None or
            self.Prohibitions is not None or
            self.Restrictions is not None or
            self.Observations is not None or
            self.Regulations is not None or
            self.AdditionalRestrictions is not None or
            self.ParcelIndemnityCoverage is not None or
            self.ExtraServices is not None or
            self.RemainingBarcodes is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='eVSPriorityMailIntlResponse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('eVSPriorityMailIntlResponse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'eVSPriorityMailIntlResponse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='eVSPriorityMailIntlResponse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='eVSPriorityMailIntlResponse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='eVSPriorityMailIntlResponse'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='eVSPriorityMailIntlResponse', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Postage is not None:
            namespaceprefix_ = self.Postage_nsprefix_ + ':' if (UseCapturedNS_ and self.Postage_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPostage>%s</%sPostage>%s' % (namespaceprefix_ , self.gds_format_float(self.Postage, input_name='Postage'), namespaceprefix_ , eol_))
        if self.TotalValue is not None:
            namespaceprefix_ = self.TotalValue_nsprefix_ + ':' if (UseCapturedNS_ and self.TotalValue_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTotalValue>%s</%sTotalValue>%s' % (namespaceprefix_ , self.gds_format_float(self.TotalValue, input_name='TotalValue'), namespaceprefix_ , eol_))
        if self.SDRValue is not None:
            namespaceprefix_ = self.SDRValue_nsprefix_ + ':' if (UseCapturedNS_ and self.SDRValue_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSDRValue>%s</%sSDRValue>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SDRValue), input_name='SDRValue')), namespaceprefix_ , eol_))
        if self.BarcodeNumber is not None:
            namespaceprefix_ = self.BarcodeNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.BarcodeNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBarcodeNumber>%s</%sBarcodeNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.BarcodeNumber), input_name='BarcodeNumber')), namespaceprefix_ , eol_))
        if self.LabelImage is not None:
            namespaceprefix_ = self.LabelImage_nsprefix_ + ':' if (UseCapturedNS_ and self.LabelImage_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sLabelImage>%s</%sLabelImage>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.LabelImage), input_name='LabelImage')), namespaceprefix_ , eol_))
        if self.Page2Image is not None:
            namespaceprefix_ = self.Page2Image_nsprefix_ + ':' if (UseCapturedNS_ and self.Page2Image_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPage2Image>%s</%sPage2Image>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Page2Image), input_name='Page2Image')), namespaceprefix_ , eol_))
        if self.Page3Image is not None:
            namespaceprefix_ = self.Page3Image_nsprefix_ + ':' if (UseCapturedNS_ and self.Page3Image_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPage3Image>%s</%sPage3Image>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Page3Image), input_name='Page3Image')), namespaceprefix_ , eol_))
        if self.Page4Image is not None:
            namespaceprefix_ = self.Page4Image_nsprefix_ + ':' if (UseCapturedNS_ and self.Page4Image_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPage4Image>%s</%sPage4Image>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Page4Image), input_name='Page4Image')), namespaceprefix_ , eol_))
        if self.Page5Image is not None:
            namespaceprefix_ = self.Page5Image_nsprefix_ + ':' if (UseCapturedNS_ and self.Page5Image_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPage5Image>%s</%sPage5Image>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Page5Image), input_name='Page5Image')), namespaceprefix_ , eol_))
        if self.Page6Image is not None:
            namespaceprefix_ = self.Page6Image_nsprefix_ + ':' if (UseCapturedNS_ and self.Page6Image_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPage6Image>%s</%sPage6Image>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Page6Image), input_name='Page6Image')), namespaceprefix_ , eol_))
        if self.Prohibitions is not None:
            namespaceprefix_ = self.Prohibitions_nsprefix_ + ':' if (UseCapturedNS_ and self.Prohibitions_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sProhibitions>%s</%sProhibitions>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Prohibitions), input_name='Prohibitions')), namespaceprefix_ , eol_))
        if self.Restrictions is not None:
            namespaceprefix_ = self.Restrictions_nsprefix_ + ':' if (UseCapturedNS_ and self.Restrictions_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRestrictions>%s</%sRestrictions>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Restrictions), input_name='Restrictions')), namespaceprefix_ , eol_))
        if self.Observations is not None:
            namespaceprefix_ = self.Observations_nsprefix_ + ':' if (UseCapturedNS_ and self.Observations_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sObservations>%s</%sObservations>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Observations), input_name='Observations')), namespaceprefix_ , eol_))
        if self.Regulations is not None:
            namespaceprefix_ = self.Regulations_nsprefix_ + ':' if (UseCapturedNS_ and self.Regulations_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRegulations>%s</%sRegulations>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Regulations), input_name='Regulations')), namespaceprefix_ , eol_))
        if self.AdditionalRestrictions is not None:
            namespaceprefix_ = self.AdditionalRestrictions_nsprefix_ + ':' if (UseCapturedNS_ and self.AdditionalRestrictions_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAdditionalRestrictions>%s</%sAdditionalRestrictions>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.AdditionalRestrictions), input_name='AdditionalRestrictions')), namespaceprefix_ , eol_))
        if self.ParcelIndemnityCoverage is not None:
            namespaceprefix_ = self.ParcelIndemnityCoverage_nsprefix_ + ':' if (UseCapturedNS_ and self.ParcelIndemnityCoverage_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sParcelIndemnityCoverage>%s</%sParcelIndemnityCoverage>%s' % (namespaceprefix_ , self.gds_format_float(self.ParcelIndemnityCoverage, input_name='ParcelIndemnityCoverage'), namespaceprefix_ , eol_))
        if self.ExtraServices is not None:
            namespaceprefix_ = self.ExtraServices_nsprefix_ + ':' if (UseCapturedNS_ and self.ExtraServices_nsprefix_) else ''
            self.ExtraServices.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ExtraServices', pretty_print=pretty_print)
        if self.RemainingBarcodes is not None:
            namespaceprefix_ = self.RemainingBarcodes_nsprefix_ + ':' if (UseCapturedNS_ and self.RemainingBarcodes_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRemainingBarcodes>%s</%sRemainingBarcodes>%s' % (namespaceprefix_ , self.gds_format_integer(self.RemainingBarcodes, input_name='RemainingBarcodes'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Postage' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_float(sval_, node, 'Postage')
            fval_ = self.gds_validate_float(fval_, node, 'Postage')
            self.Postage = fval_
            self.Postage_nsprefix_ = child_.prefix
        elif nodeName_ == 'TotalValue' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_float(sval_, node, 'TotalValue')
            fval_ = self.gds_validate_float(fval_, node, 'TotalValue')
            self.TotalValue = fval_
            self.TotalValue_nsprefix_ = child_.prefix
        elif nodeName_ == 'SDRValue':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SDRValue')
            value_ = self.gds_validate_string(value_, node, 'SDRValue')
            self.SDRValue = value_
            self.SDRValue_nsprefix_ = child_.prefix
        elif nodeName_ == 'BarcodeNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'BarcodeNumber')
            value_ = self.gds_validate_string(value_, node, 'BarcodeNumber')
            self.BarcodeNumber = value_
            self.BarcodeNumber_nsprefix_ = child_.prefix
        elif nodeName_ == 'LabelImage':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'LabelImage')
            value_ = self.gds_validate_string(value_, node, 'LabelImage')
            self.LabelImage = value_
            self.LabelImage_nsprefix_ = child_.prefix
        elif nodeName_ == 'Page2Image':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Page2Image')
            value_ = self.gds_validate_string(value_, node, 'Page2Image')
            self.Page2Image = value_
            self.Page2Image_nsprefix_ = child_.prefix
        elif nodeName_ == 'Page3Image':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Page3Image')
            value_ = self.gds_validate_string(value_, node, 'Page3Image')
            self.Page3Image = value_
            self.Page3Image_nsprefix_ = child_.prefix
        elif nodeName_ == 'Page4Image':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Page4Image')
            value_ = self.gds_validate_string(value_, node, 'Page4Image')
            self.Page4Image = value_
            self.Page4Image_nsprefix_ = child_.prefix
        elif nodeName_ == 'Page5Image':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Page5Image')
            value_ = self.gds_validate_string(value_, node, 'Page5Image')
            self.Page5Image = value_
            self.Page5Image_nsprefix_ = child_.prefix
        elif nodeName_ == 'Page6Image':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Page6Image')
            value_ = self.gds_validate_string(value_, node, 'Page6Image')
            self.Page6Image = value_
            self.Page6Image_nsprefix_ = child_.prefix
        elif nodeName_ == 'Prohibitions':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Prohibitions')
            value_ = self.gds_validate_string(value_, node, 'Prohibitions')
            self.Prohibitions = value_
            self.Prohibitions_nsprefix_ = child_.prefix
        elif nodeName_ == 'Restrictions':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Restrictions')
            value_ = self.gds_validate_string(value_, node, 'Restrictions')
            self.Restrictions = value_
            self.Restrictions_nsprefix_ = child_.prefix
        elif nodeName_ == 'Observations':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Observations')
            value_ = self.gds_validate_string(value_, node, 'Observations')
            self.Observations = value_
            self.Observations_nsprefix_ = child_.prefix
        elif nodeName_ == 'Regulations':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Regulations')
            value_ = self.gds_validate_string(value_, node, 'Regulations')
            self.Regulations = value_
            self.Regulations_nsprefix_ = child_.prefix
        elif nodeName_ == 'AdditionalRestrictions':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'AdditionalRestrictions')
            value_ = self.gds_validate_string(value_, node, 'AdditionalRestrictions')
            self.AdditionalRestrictions = value_
            self.AdditionalRestrictions_nsprefix_ = child_.prefix
        elif nodeName_ == 'ParcelIndemnityCoverage' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_float(sval_, node, 'ParcelIndemnityCoverage')
            fval_ = self.gds_validate_float(fval_, node, 'ParcelIndemnityCoverage')
            self.ParcelIndemnityCoverage = fval_
            self.ParcelIndemnityCoverage_nsprefix_ = child_.prefix
        elif nodeName_ == 'ExtraServices':
            obj_ = ExtraServicesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ExtraServices = obj_
            obj_.original_tagname_ = 'ExtraServices'
        elif nodeName_ == 'RemainingBarcodes' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'RemainingBarcodes')
            ival_ = self.gds_validate_integer(ival_, node, 'RemainingBarcodes')
            self.RemainingBarcodes = ival_
            self.RemainingBarcodes_nsprefix_ = child_.prefix
# end class eVSPriorityMailIntlResponse


class ExtraServicesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ExtraService=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if ExtraService is None:
            self.ExtraService = []
        else:
            self.ExtraService = ExtraService
        self.ExtraService_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ExtraServicesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ExtraServicesType.subclass:
            return ExtraServicesType.subclass(*args_, **kwargs_)
        else:
            return ExtraServicesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ExtraService(self):
        return self.ExtraService
    def set_ExtraService(self, ExtraService):
        self.ExtraService = ExtraService
    def add_ExtraService(self, value):
        self.ExtraService.append(value)
    def insert_ExtraService_at(self, index, value):
        self.ExtraService.insert(index, value)
    def replace_ExtraService_at(self, index, value):
        self.ExtraService[index] = value
    def hasContent_(self):
        if (
            self.ExtraService
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ExtraServicesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ExtraServicesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ExtraServicesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ExtraServicesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ExtraServicesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ExtraServicesType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ExtraServicesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for ExtraService_ in self.ExtraService:
            namespaceprefix_ = self.ExtraService_nsprefix_ + ':' if (UseCapturedNS_ and self.ExtraService_nsprefix_) else ''
            ExtraService_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ExtraService', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ExtraService':
            obj_ = ExtraServiceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ExtraService.append(obj_)
            obj_.original_tagname_ = 'ExtraService'
# end class ExtraServicesType


class ExtraServiceType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ServiceID=None, ServiceName=None, Price=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ServiceID = ServiceID
        self.ServiceID_nsprefix_ = None
        self.ServiceName = ServiceName
        self.ServiceName_nsprefix_ = None
        self.Price = Price
        self.Price_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ExtraServiceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ExtraServiceType.subclass:
            return ExtraServiceType.subclass(*args_, **kwargs_)
        else:
            return ExtraServiceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ServiceID(self):
        return self.ServiceID
    def set_ServiceID(self, ServiceID):
        self.ServiceID = ServiceID
    def get_ServiceName(self):
        return self.ServiceName
    def set_ServiceName(self, ServiceName):
        self.ServiceName = ServiceName
    def get_Price(self):
        return self.Price
    def set_Price(self, Price):
        self.Price = Price
    def hasContent_(self):
        if (
            self.ServiceID is not None or
            self.ServiceName is not None or
            self.Price is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ExtraServiceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ExtraServiceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ExtraServiceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ExtraServiceType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ExtraServiceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ExtraServiceType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ExtraServiceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ServiceID is not None:
            namespaceprefix_ = self.ServiceID_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sServiceID>%s</%sServiceID>%s' % (namespaceprefix_ , self.gds_format_integer(self.ServiceID, input_name='ServiceID'), namespaceprefix_ , eol_))
        if self.ServiceName is not None:
            namespaceprefix_ = self.ServiceName_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sServiceName>%s</%sServiceName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ServiceName), input_name='ServiceName')), namespaceprefix_ , eol_))
        if self.Price is not None:
            namespaceprefix_ = self.Price_nsprefix_ + ':' if (UseCapturedNS_ and self.Price_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPrice>%s</%sPrice>%s' % (namespaceprefix_ , self.gds_format_float(self.Price, input_name='Price'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ServiceID' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'ServiceID')
            ival_ = self.gds_validate_integer(ival_, node, 'ServiceID')
            self.ServiceID = ival_
            self.ServiceID_nsprefix_ = child_.prefix
        elif nodeName_ == 'ServiceName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ServiceName')
            value_ = self.gds_validate_string(value_, node, 'ServiceName')
            self.ServiceName = value_
            self.ServiceName_nsprefix_ = child_.prefix
        elif nodeName_ == 'Price' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_float(sval_, node, 'Price')
            fval_ = self.gds_validate_float(fval_, node, 'Price')
            self.Price = fval_
            self.Price_nsprefix_ = child_.prefix
# end class ExtraServiceType


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
        rootTag = 'eVSPriorityMailIntlResponse'
        rootClass = eVSPriorityMailIntlResponse
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
        rootTag = 'eVSPriorityMailIntlResponse'
        rootClass = eVSPriorityMailIntlResponse
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
        rootTag = 'eVSPriorityMailIntlResponse'
        rootClass = eVSPriorityMailIntlResponse
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
        rootTag = 'eVSPriorityMailIntlResponse'
        rootClass = eVSPriorityMailIntlResponse
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from evs_priority_mail_intl_response import *\n\n')
        sys.stdout.write('import evs_priority_mail_intl_response as model_\n\n')
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
NamespaceToDefMappings_ = {}

__all__ = [
    "ExtraServiceType",
    "ExtraServicesType",
    "eVSPriorityMailIntlResponse"
]
