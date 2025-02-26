#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Wed Nov 10 10:01:04 2021 by generateDS.py version 2.40.5.
# Python 3.8.6 (v3.8.6:db455296be, Sep 23 2020, 13:31:39)  [Clang 6.0 (clang-600.0.57)]
#
# Command line options:
#   ('--no-namespace-defs', '')
#   ('-o', './ups_lib/time_in_transit_web_service_schema.py')
#
# Command line arguments:
#   ./schemas/TimeInTransitWebServiceSchema.xsd
#
# Command line:
#   /Users/danielkobina/Workspace/project/karrio/.venv/karrio/bin/generateDS --no-namespace-defs -o "./ups_lib/time_in_transit_web_service_schema.py" ./schemas/TimeInTransitWebServiceSchema.xsd
#
# Current working directory (os.getcwd()):
#   ups
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
from lxml import etree as etree_


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
        def __str__(self):
            settings = {
                'str_pretty_print': True,
                'str_indent_level': 0,
                'str_namespaceprefix': '',
                'str_name': None,
                'str_namespacedefs': '',
            }
            for n in settings:
                if hasattr(self, n):
                    setattr(settings[n], self[n])
            from io import StringIO
            output = StringIO()
            self.export(
                output,
                settings['str_indent_level'],
                pretty_print=settings['str_pretty_print'],
                namespaceprefix_=settings['str_namespaceprefix'],
                name_=settings['str_name'],
                namespacedef_=settings['str_namespacedefs']
            )
            strval = output.getvalue()
            output.close()
            return strval
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
            return base64.b64encode(input_data).decode('ascii')
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % int(input_data)
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
            return ('%.15f' % float(input_data)).rstrip('0')
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
    def to_etree(self, element, mapping_=None, reverse_mapping_=None, nsmap_=None):
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
    def to_etree_simple(self, mapping_=None, reverse_mapping_=None, nsmap_=None):
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


class ResponseShipListAddressType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Town=None, City=None, StateProvinceCode=None, CountryCode=None, PostcodePrimaryLow=None, PostcodePrimaryHigh=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Town = Town
        self.Town_nsprefix_ = None
        self.City = City
        self.City_nsprefix_ = None
        self.StateProvinceCode = StateProvinceCode
        self.StateProvinceCode_nsprefix_ = None
        self.CountryCode = CountryCode
        self.CountryCode_nsprefix_ = None
        self.PostcodePrimaryLow = PostcodePrimaryLow
        self.PostcodePrimaryLow_nsprefix_ = None
        self.PostcodePrimaryHigh = PostcodePrimaryHigh
        self.PostcodePrimaryHigh_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ResponseShipListAddressType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ResponseShipListAddressType.subclass:
            return ResponseShipListAddressType.subclass(*args_, **kwargs_)
        else:
            return ResponseShipListAddressType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Town(self):
        return self.Town
    def set_Town(self, Town):
        self.Town = Town
    def get_City(self):
        return self.City
    def set_City(self, City):
        self.City = City
    def get_StateProvinceCode(self):
        return self.StateProvinceCode
    def set_StateProvinceCode(self, StateProvinceCode):
        self.StateProvinceCode = StateProvinceCode
    def get_CountryCode(self):
        return self.CountryCode
    def set_CountryCode(self, CountryCode):
        self.CountryCode = CountryCode
    def get_PostcodePrimaryLow(self):
        return self.PostcodePrimaryLow
    def set_PostcodePrimaryLow(self, PostcodePrimaryLow):
        self.PostcodePrimaryLow = PostcodePrimaryLow
    def get_PostcodePrimaryHigh(self):
        return self.PostcodePrimaryHigh
    def set_PostcodePrimaryHigh(self, PostcodePrimaryHigh):
        self.PostcodePrimaryHigh = PostcodePrimaryHigh
    def _hasContent(self):
        if (
            self.Town is not None or
            self.City is not None or
            self.StateProvinceCode is not None or
            self.CountryCode is not None or
            self.PostcodePrimaryLow is not None or
            self.PostcodePrimaryHigh is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ResponseShipListAddressType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ResponseShipListAddressType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ResponseShipListAddressType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ResponseShipListAddressType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ResponseShipListAddressType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ResponseShipListAddressType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ResponseShipListAddressType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Town is not None:
            namespaceprefix_ = self.Town_nsprefix_ + ':' if (UseCapturedNS_ and self.Town_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTown>%s</%sTown>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Town), input_name='Town')), namespaceprefix_ , eol_))
        if self.City is not None:
            namespaceprefix_ = self.City_nsprefix_ + ':' if (UseCapturedNS_ and self.City_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCity>%s</%sCity>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.City), input_name='City')), namespaceprefix_ , eol_))
        if self.StateProvinceCode is not None:
            namespaceprefix_ = self.StateProvinceCode_nsprefix_ + ':' if (UseCapturedNS_ and self.StateProvinceCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sStateProvinceCode>%s</%sStateProvinceCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.StateProvinceCode), input_name='StateProvinceCode')), namespaceprefix_ , eol_))
        if self.CountryCode is not None:
            namespaceprefix_ = self.CountryCode_nsprefix_ + ':' if (UseCapturedNS_ and self.CountryCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCountryCode>%s</%sCountryCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CountryCode), input_name='CountryCode')), namespaceprefix_ , eol_))
        if self.PostcodePrimaryLow is not None:
            namespaceprefix_ = self.PostcodePrimaryLow_nsprefix_ + ':' if (UseCapturedNS_ and self.PostcodePrimaryLow_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPostcodePrimaryLow>%s</%sPostcodePrimaryLow>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.PostcodePrimaryLow), input_name='PostcodePrimaryLow')), namespaceprefix_ , eol_))
        if self.PostcodePrimaryHigh is not None:
            namespaceprefix_ = self.PostcodePrimaryHigh_nsprefix_ + ':' if (UseCapturedNS_ and self.PostcodePrimaryHigh_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPostcodePrimaryHigh>%s</%sPostcodePrimaryHigh>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.PostcodePrimaryHigh), input_name='PostcodePrimaryHigh')), namespaceprefix_ , eol_))
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Town':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Town')
            value_ = self.gds_validate_string(value_, node, 'Town')
            self.Town = value_
            self.Town_nsprefix_ = child_.prefix
        elif nodeName_ == 'City':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'City')
            value_ = self.gds_validate_string(value_, node, 'City')
            self.City = value_
            self.City_nsprefix_ = child_.prefix
        elif nodeName_ == 'StateProvinceCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'StateProvinceCode')
            value_ = self.gds_validate_string(value_, node, 'StateProvinceCode')
            self.StateProvinceCode = value_
            self.StateProvinceCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'CountryCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CountryCode')
            value_ = self.gds_validate_string(value_, node, 'CountryCode')
            self.CountryCode = value_
            self.CountryCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'PostcodePrimaryLow':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'PostcodePrimaryLow')
            value_ = self.gds_validate_string(value_, node, 'PostcodePrimaryLow')
            self.PostcodePrimaryLow = value_
            self.PostcodePrimaryLow_nsprefix_ = child_.prefix
        elif nodeName_ == 'PostcodePrimaryHigh':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'PostcodePrimaryHigh')
            value_ = self.gds_validate_string(value_, node, 'PostcodePrimaryHigh')
            self.PostcodePrimaryHigh = value_
            self.PostcodePrimaryHigh_nsprefix_ = child_.prefix
# end class ResponseShipListAddressType


class RequestShipFromAddressType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Town=None, City=None, StateProvinceCode=None, CountryCode=None, PostalCode=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Town = Town
        self.Town_nsprefix_ = None
        self.City = City
        self.City_nsprefix_ = None
        self.StateProvinceCode = StateProvinceCode
        self.StateProvinceCode_nsprefix_ = None
        self.CountryCode = CountryCode
        self.CountryCode_nsprefix_ = None
        self.PostalCode = PostalCode
        self.PostalCode_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RequestShipFromAddressType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RequestShipFromAddressType.subclass:
            return RequestShipFromAddressType.subclass(*args_, **kwargs_)
        else:
            return RequestShipFromAddressType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Town(self):
        return self.Town
    def set_Town(self, Town):
        self.Town = Town
    def get_City(self):
        return self.City
    def set_City(self, City):
        self.City = City
    def get_StateProvinceCode(self):
        return self.StateProvinceCode
    def set_StateProvinceCode(self, StateProvinceCode):
        self.StateProvinceCode = StateProvinceCode
    def get_CountryCode(self):
        return self.CountryCode
    def set_CountryCode(self, CountryCode):
        self.CountryCode = CountryCode
    def get_PostalCode(self):
        return self.PostalCode
    def set_PostalCode(self, PostalCode):
        self.PostalCode = PostalCode
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def _hasContent(self):
        if (
            self.Town is not None or
            self.City is not None or
            self.StateProvinceCode is not None or
            self.CountryCode is not None or
            self.PostalCode is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RequestShipFromAddressType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RequestShipFromAddressType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RequestShipFromAddressType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RequestShipFromAddressType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RequestShipFromAddressType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RequestShipFromAddressType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RequestShipFromAddressType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Town is not None:
            namespaceprefix_ = self.Town_nsprefix_ + ':' if (UseCapturedNS_ and self.Town_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTown>%s</%sTown>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Town), input_name='Town')), namespaceprefix_ , eol_))
        if self.City is not None:
            namespaceprefix_ = self.City_nsprefix_ + ':' if (UseCapturedNS_ and self.City_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCity>%s</%sCity>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.City), input_name='City')), namespaceprefix_ , eol_))
        if self.StateProvinceCode is not None:
            namespaceprefix_ = self.StateProvinceCode_nsprefix_ + ':' if (UseCapturedNS_ and self.StateProvinceCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sStateProvinceCode>%s</%sStateProvinceCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.StateProvinceCode), input_name='StateProvinceCode')), namespaceprefix_ , eol_))
        if self.CountryCode is not None:
            namespaceprefix_ = self.CountryCode_nsprefix_ + ':' if (UseCapturedNS_ and self.CountryCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCountryCode>%s</%sCountryCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CountryCode), input_name='CountryCode')), namespaceprefix_ , eol_))
        if self.PostalCode is not None:
            namespaceprefix_ = self.PostalCode_nsprefix_ + ':' if (UseCapturedNS_ and self.PostalCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPostalCode>%s</%sPostalCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.PostalCode), input_name='PostalCode')), namespaceprefix_ , eol_))
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
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Town':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Town')
            value_ = self.gds_validate_string(value_, node, 'Town')
            self.Town = value_
            self.Town_nsprefix_ = child_.prefix
        elif nodeName_ == 'City':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'City')
            value_ = self.gds_validate_string(value_, node, 'City')
            self.City = value_
            self.City_nsprefix_ = child_.prefix
        elif nodeName_ == 'StateProvinceCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'StateProvinceCode')
            value_ = self.gds_validate_string(value_, node, 'StateProvinceCode')
            self.StateProvinceCode = value_
            self.StateProvinceCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'CountryCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CountryCode')
            value_ = self.gds_validate_string(value_, node, 'CountryCode')
            self.CountryCode = value_
            self.CountryCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'PostalCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'PostalCode')
            value_ = self.gds_validate_string(value_, node, 'PostalCode')
            self.PostalCode = value_
            self.PostalCode_nsprefix_ = child_.prefix
# end class RequestShipFromAddressType


class RequestShipToAddressType(RequestShipFromAddressType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = RequestShipFromAddressType
    def __init__(self, Town=None, City=None, StateProvinceCode=None, CountryCode=None, PostalCode=None, ResidentialAddressIndicator=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("RequestShipToAddressType"), self).__init__(Town, City, StateProvinceCode, CountryCode, PostalCode,  **kwargs_)
        self.ResidentialAddressIndicator = ResidentialAddressIndicator
        self.ResidentialAddressIndicator_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RequestShipToAddressType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RequestShipToAddressType.subclass:
            return RequestShipToAddressType.subclass(*args_, **kwargs_)
        else:
            return RequestShipToAddressType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ResidentialAddressIndicator(self):
        return self.ResidentialAddressIndicator
    def set_ResidentialAddressIndicator(self, ResidentialAddressIndicator):
        self.ResidentialAddressIndicator = ResidentialAddressIndicator
    def _hasContent(self):
        if (
            self.ResidentialAddressIndicator is not None or
            super(RequestShipToAddressType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RequestShipToAddressType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RequestShipToAddressType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RequestShipToAddressType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RequestShipToAddressType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RequestShipToAddressType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RequestShipToAddressType'):
        super(RequestShipToAddressType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RequestShipToAddressType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RequestShipToAddressType', fromsubclass_=False, pretty_print=True):
        super(RequestShipToAddressType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ResidentialAddressIndicator is not None:
            namespaceprefix_ = self.ResidentialAddressIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.ResidentialAddressIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sResidentialAddressIndicator>%s</%sResidentialAddressIndicator>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ResidentialAddressIndicator), input_name='ResidentialAddressIndicator')), namespaceprefix_ , eol_))
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
        super(RequestShipToAddressType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ResidentialAddressIndicator':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ResidentialAddressIndicator')
            value_ = self.gds_validate_string(value_, node, 'ResidentialAddressIndicator')
            self.ResidentialAddressIndicator = value_
            self.ResidentialAddressIndicator_nsprefix_ = child_.prefix
        super(RequestShipToAddressType, self)._buildChildren(child_, node, nodeName_, True)
# end class RequestShipToAddressType


class ResponseShipFromAddressType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Town=None, City=None, StateProvinceCode=None, CountryCode=None, Country=None, PostalCode=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Town = Town
        self.Town_nsprefix_ = None
        self.City = City
        self.City_nsprefix_ = None
        self.StateProvinceCode = StateProvinceCode
        self.StateProvinceCode_nsprefix_ = None
        self.CountryCode = CountryCode
        self.CountryCode_nsprefix_ = None
        self.Country = Country
        self.Country_nsprefix_ = None
        self.PostalCode = PostalCode
        self.PostalCode_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ResponseShipFromAddressType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ResponseShipFromAddressType.subclass:
            return ResponseShipFromAddressType.subclass(*args_, **kwargs_)
        else:
            return ResponseShipFromAddressType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Town(self):
        return self.Town
    def set_Town(self, Town):
        self.Town = Town
    def get_City(self):
        return self.City
    def set_City(self, City):
        self.City = City
    def get_StateProvinceCode(self):
        return self.StateProvinceCode
    def set_StateProvinceCode(self, StateProvinceCode):
        self.StateProvinceCode = StateProvinceCode
    def get_CountryCode(self):
        return self.CountryCode
    def set_CountryCode(self, CountryCode):
        self.CountryCode = CountryCode
    def get_Country(self):
        return self.Country
    def set_Country(self, Country):
        self.Country = Country
    def get_PostalCode(self):
        return self.PostalCode
    def set_PostalCode(self, PostalCode):
        self.PostalCode = PostalCode
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def _hasContent(self):
        if (
            self.Town is not None or
            self.City is not None or
            self.StateProvinceCode is not None or
            self.CountryCode is not None or
            self.Country is not None or
            self.PostalCode is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ResponseShipFromAddressType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ResponseShipFromAddressType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ResponseShipFromAddressType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ResponseShipFromAddressType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ResponseShipFromAddressType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ResponseShipFromAddressType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ResponseShipFromAddressType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Town is not None:
            namespaceprefix_ = self.Town_nsprefix_ + ':' if (UseCapturedNS_ and self.Town_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTown>%s</%sTown>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Town), input_name='Town')), namespaceprefix_ , eol_))
        if self.City is not None:
            namespaceprefix_ = self.City_nsprefix_ + ':' if (UseCapturedNS_ and self.City_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCity>%s</%sCity>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.City), input_name='City')), namespaceprefix_ , eol_))
        if self.StateProvinceCode is not None:
            namespaceprefix_ = self.StateProvinceCode_nsprefix_ + ':' if (UseCapturedNS_ and self.StateProvinceCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sStateProvinceCode>%s</%sStateProvinceCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.StateProvinceCode), input_name='StateProvinceCode')), namespaceprefix_ , eol_))
        if self.CountryCode is not None:
            namespaceprefix_ = self.CountryCode_nsprefix_ + ':' if (UseCapturedNS_ and self.CountryCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCountryCode>%s</%sCountryCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CountryCode), input_name='CountryCode')), namespaceprefix_ , eol_))
        if self.Country is not None:
            namespaceprefix_ = self.Country_nsprefix_ + ':' if (UseCapturedNS_ and self.Country_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCountry>%s</%sCountry>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Country), input_name='Country')), namespaceprefix_ , eol_))
        if self.PostalCode is not None:
            namespaceprefix_ = self.PostalCode_nsprefix_ + ':' if (UseCapturedNS_ and self.PostalCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPostalCode>%s</%sPostalCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.PostalCode), input_name='PostalCode')), namespaceprefix_ , eol_))
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
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Town':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Town')
            value_ = self.gds_validate_string(value_, node, 'Town')
            self.Town = value_
            self.Town_nsprefix_ = child_.prefix
        elif nodeName_ == 'City':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'City')
            value_ = self.gds_validate_string(value_, node, 'City')
            self.City = value_
            self.City_nsprefix_ = child_.prefix
        elif nodeName_ == 'StateProvinceCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'StateProvinceCode')
            value_ = self.gds_validate_string(value_, node, 'StateProvinceCode')
            self.StateProvinceCode = value_
            self.StateProvinceCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'CountryCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CountryCode')
            value_ = self.gds_validate_string(value_, node, 'CountryCode')
            self.CountryCode = value_
            self.CountryCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'Country':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Country')
            value_ = self.gds_validate_string(value_, node, 'Country')
            self.Country = value_
            self.Country_nsprefix_ = child_.prefix
        elif nodeName_ == 'PostalCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'PostalCode')
            value_ = self.gds_validate_string(value_, node, 'PostalCode')
            self.PostalCode = value_
            self.PostalCode_nsprefix_ = child_.prefix
# end class ResponseShipFromAddressType


class ResponseShipToAddressType(ResponseShipFromAddressType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = ResponseShipFromAddressType
    def __init__(self, Town=None, City=None, StateProvinceCode=None, CountryCode=None, Country=None, PostalCode=None, ResidentialAddressIndicator=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("ResponseShipToAddressType"), self).__init__(Town, City, StateProvinceCode, CountryCode, Country, PostalCode,  **kwargs_)
        self.ResidentialAddressIndicator = ResidentialAddressIndicator
        self.ResidentialAddressIndicator_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ResponseShipToAddressType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ResponseShipToAddressType.subclass:
            return ResponseShipToAddressType.subclass(*args_, **kwargs_)
        else:
            return ResponseShipToAddressType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ResidentialAddressIndicator(self):
        return self.ResidentialAddressIndicator
    def set_ResidentialAddressIndicator(self, ResidentialAddressIndicator):
        self.ResidentialAddressIndicator = ResidentialAddressIndicator
    def _hasContent(self):
        if (
            self.ResidentialAddressIndicator is not None or
            super(ResponseShipToAddressType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ResponseShipToAddressType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ResponseShipToAddressType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ResponseShipToAddressType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ResponseShipToAddressType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ResponseShipToAddressType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ResponseShipToAddressType'):
        super(ResponseShipToAddressType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ResponseShipToAddressType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ResponseShipToAddressType', fromsubclass_=False, pretty_print=True):
        super(ResponseShipToAddressType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ResidentialAddressIndicator is not None:
            namespaceprefix_ = self.ResidentialAddressIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.ResidentialAddressIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sResidentialAddressIndicator>%s</%sResidentialAddressIndicator>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ResidentialAddressIndicator), input_name='ResidentialAddressIndicator')), namespaceprefix_ , eol_))
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
        super(ResponseShipToAddressType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ResidentialAddressIndicator':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ResidentialAddressIndicator')
            value_ = self.gds_validate_string(value_, node, 'ResidentialAddressIndicator')
            self.ResidentialAddressIndicator = value_
            self.ResidentialAddressIndicator_nsprefix_ = child_.prefix
        super(ResponseShipToAddressType, self)._buildChildren(child_, node, nodeName_, True)
# end class ResponseShipToAddressType


class RequestShipFromType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Address=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Address = Address
        self.Address_nsprefix_ = "tnt"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RequestShipFromType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RequestShipFromType.subclass:
            return RequestShipFromType.subclass(*args_, **kwargs_)
        else:
            return RequestShipFromType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Address(self):
        return self.Address
    def set_Address(self, Address):
        self.Address = Address
    def _hasContent(self):
        if (
            self.Address is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RequestShipFromType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RequestShipFromType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RequestShipFromType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RequestShipFromType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RequestShipFromType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RequestShipFromType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RequestShipFromType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Address is not None:
            namespaceprefix_ = self.Address_nsprefix_ + ':' if (UseCapturedNS_ and self.Address_nsprefix_) else ''
            self.Address.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Address', pretty_print=pretty_print)
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Address':
            class_obj_ = self.get_class_obj_(child_, RequestShipFromAddressType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Address = obj_
            obj_.original_tagname_ = 'Address'
# end class RequestShipFromType


class RequestShipToType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Address=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Address = Address
        self.Address_nsprefix_ = "tnt"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RequestShipToType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RequestShipToType.subclass:
            return RequestShipToType.subclass(*args_, **kwargs_)
        else:
            return RequestShipToType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Address(self):
        return self.Address
    def set_Address(self, Address):
        self.Address = Address
    def _hasContent(self):
        if (
            self.Address is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RequestShipToType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RequestShipToType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RequestShipToType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RequestShipToType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RequestShipToType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RequestShipToType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RequestShipToType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Address is not None:
            namespaceprefix_ = self.Address_nsprefix_ + ':' if (UseCapturedNS_ and self.Address_nsprefix_) else ''
            self.Address.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Address', pretty_print=pretty_print)
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Address':
            obj_ = RequestShipToAddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Address = obj_
            obj_.original_tagname_ = 'Address'
# end class RequestShipToType


class ResponseShipFromType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Address=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Address = Address
        self.Address_nsprefix_ = "tnt"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ResponseShipFromType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ResponseShipFromType.subclass:
            return ResponseShipFromType.subclass(*args_, **kwargs_)
        else:
            return ResponseShipFromType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Address(self):
        return self.Address
    def set_Address(self, Address):
        self.Address = Address
    def _hasContent(self):
        if (
            self.Address is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ResponseShipFromType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ResponseShipFromType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ResponseShipFromType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ResponseShipFromType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ResponseShipFromType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ResponseShipFromType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ResponseShipFromType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Address is not None:
            namespaceprefix_ = self.Address_nsprefix_ + ':' if (UseCapturedNS_ and self.Address_nsprefix_) else ''
            self.Address.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Address', pretty_print=pretty_print)
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Address':
            class_obj_ = self.get_class_obj_(child_, ResponseShipFromAddressType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Address = obj_
            obj_.original_tagname_ = 'Address'
# end class ResponseShipFromType


class ResponseShipToType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Address=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Address = Address
        self.Address_nsprefix_ = "tnt"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ResponseShipToType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ResponseShipToType.subclass:
            return ResponseShipToType.subclass(*args_, **kwargs_)
        else:
            return ResponseShipToType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Address(self):
        return self.Address
    def set_Address(self, Address):
        self.Address = Address
    def _hasContent(self):
        if (
            self.Address is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ResponseShipToType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ResponseShipToType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ResponseShipToType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ResponseShipToType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ResponseShipToType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ResponseShipToType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ResponseShipToType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Address is not None:
            namespaceprefix_ = self.Address_nsprefix_ + ':' if (UseCapturedNS_ and self.Address_nsprefix_) else ''
            self.Address.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Address', pretty_print=pretty_print)
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Address':
            obj_ = ResponseShipToAddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Address = obj_
            obj_.original_tagname_ = 'Address'
# end class ResponseShipToType


class ShipmentWeightType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, UnitOfMeasurement=None, Weight=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.UnitOfMeasurement = UnitOfMeasurement
        self.UnitOfMeasurement_nsprefix_ = None
        self.Weight = Weight
        self.Weight_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ShipmentWeightType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ShipmentWeightType.subclass:
            return ShipmentWeightType.subclass(*args_, **kwargs_)
        else:
            return ShipmentWeightType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_UnitOfMeasurement(self):
        return self.UnitOfMeasurement
    def set_UnitOfMeasurement(self, UnitOfMeasurement):
        self.UnitOfMeasurement = UnitOfMeasurement
    def get_Weight(self):
        return self.Weight
    def set_Weight(self, Weight):
        self.Weight = Weight
    def _hasContent(self):
        if (
            self.UnitOfMeasurement is not None or
            self.Weight is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentWeightType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ShipmentWeightType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ShipmentWeightType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ShipmentWeightType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ShipmentWeightType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ShipmentWeightType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentWeightType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.UnitOfMeasurement is not None:
            namespaceprefix_ = self.UnitOfMeasurement_nsprefix_ + ':' if (UseCapturedNS_ and self.UnitOfMeasurement_nsprefix_) else ''
            self.UnitOfMeasurement.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UnitOfMeasurement', pretty_print=pretty_print)
        if self.Weight is not None:
            namespaceprefix_ = self.Weight_nsprefix_ + ':' if (UseCapturedNS_ and self.Weight_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sWeight>%s</%sWeight>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Weight), input_name='Weight')), namespaceprefix_ , eol_))
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'UnitOfMeasurement':
            obj_ = CodeDescriptionType1.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UnitOfMeasurement = obj_
            obj_.original_tagname_ = 'UnitOfMeasurement'
        elif nodeName_ == 'Weight':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Weight')
            value_ = self.gds_validate_string(value_, node, 'Weight')
            self.Weight = value_
            self.Weight_nsprefix_ = child_.prefix
# end class ShipmentWeightType


class CodeDescriptionType1(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Code=None, Description=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Code = Code
        self.Code_nsprefix_ = None
        self.Description = Description
        self.Description_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CodeDescriptionType1)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CodeDescriptionType1.subclass:
            return CodeDescriptionType1.subclass(*args_, **kwargs_)
        else:
            return CodeDescriptionType1(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Code(self):
        return self.Code
    def set_Code(self, Code):
        self.Code = Code
    def get_Description(self):
        return self.Description
    def set_Description(self, Description):
        self.Description = Description
    def _hasContent(self):
        if (
            self.Code is not None or
            self.Description is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CodeDescriptionType1', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CodeDescriptionType1')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CodeDescriptionType1':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CodeDescriptionType1')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CodeDescriptionType1', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CodeDescriptionType1'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CodeDescriptionType1', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Code is not None:
            namespaceprefix_ = self.Code_nsprefix_ + ':' if (UseCapturedNS_ and self.Code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCode>%s</%sCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Code), input_name='Code')), namespaceprefix_ , eol_))
        if self.Description is not None:
            namespaceprefix_ = self.Description_nsprefix_ + ':' if (UseCapturedNS_ and self.Description_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDescription>%s</%sDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Description), input_name='Description')), namespaceprefix_ , eol_))
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Code')
            value_ = self.gds_validate_string(value_, node, 'Code')
            self.Code = value_
            self.Code_nsprefix_ = child_.prefix
        elif nodeName_ == 'Description':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Description')
            value_ = self.gds_validate_string(value_, node, 'Description')
            self.Description = value_
            self.Description_nsprefix_ = child_.prefix
# end class CodeDescriptionType1


class PickupType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Date=None, Time=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Date = Date
        self.Date_nsprefix_ = None
        self.Time = Time
        self.Time_nsprefix_ = None
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
    def get_Date(self):
        return self.Date
    def set_Date(self, Date):
        self.Date = Date
    def get_Time(self):
        return self.Time
    def set_Time(self, Time):
        self.Time = Time
    def _hasContent(self):
        if (
            self.Date is not None or
            self.Time is not None
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
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PickupType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PickupType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Date is not None:
            namespaceprefix_ = self.Date_nsprefix_ + ':' if (UseCapturedNS_ and self.Date_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDate>%s</%sDate>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Date), input_name='Date')), namespaceprefix_ , eol_))
        if self.Time is not None:
            namespaceprefix_ = self.Time_nsprefix_ + ':' if (UseCapturedNS_ and self.Time_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTime>%s</%sTime>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Time), input_name='Time')), namespaceprefix_ , eol_))
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Date':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Date')
            value_ = self.gds_validate_string(value_, node, 'Date')
            self.Date = value_
            self.Date_nsprefix_ = child_.prefix
        elif nodeName_ == 'Time':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Time')
            value_ = self.gds_validate_string(value_, node, 'Time')
            self.Time = value_
            self.Time_nsprefix_ = child_.prefix
# end class PickupType


class InvoiceLineTotalType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, CurrencyCode=None, MonetaryValue=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.CurrencyCode = CurrencyCode
        self.CurrencyCode_nsprefix_ = None
        self.MonetaryValue = MonetaryValue
        self.MonetaryValue_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InvoiceLineTotalType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InvoiceLineTotalType.subclass:
            return InvoiceLineTotalType.subclass(*args_, **kwargs_)
        else:
            return InvoiceLineTotalType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_CurrencyCode(self):
        return self.CurrencyCode
    def set_CurrencyCode(self, CurrencyCode):
        self.CurrencyCode = CurrencyCode
    def get_MonetaryValue(self):
        return self.MonetaryValue
    def set_MonetaryValue(self, MonetaryValue):
        self.MonetaryValue = MonetaryValue
    def _hasContent(self):
        if (
            self.CurrencyCode is not None or
            self.MonetaryValue is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='InvoiceLineTotalType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InvoiceLineTotalType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InvoiceLineTotalType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InvoiceLineTotalType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InvoiceLineTotalType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='InvoiceLineTotalType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='InvoiceLineTotalType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CurrencyCode is not None:
            namespaceprefix_ = self.CurrencyCode_nsprefix_ + ':' if (UseCapturedNS_ and self.CurrencyCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCurrencyCode>%s</%sCurrencyCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CurrencyCode), input_name='CurrencyCode')), namespaceprefix_ , eol_))
        if self.MonetaryValue is not None:
            namespaceprefix_ = self.MonetaryValue_nsprefix_ + ':' if (UseCapturedNS_ and self.MonetaryValue_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMonetaryValue>%s</%sMonetaryValue>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.MonetaryValue), input_name='MonetaryValue')), namespaceprefix_ , eol_))
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CurrencyCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CurrencyCode')
            value_ = self.gds_validate_string(value_, node, 'CurrencyCode')
            self.CurrencyCode = value_
            self.CurrencyCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'MonetaryValue':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'MonetaryValue')
            value_ = self.gds_validate_string(value_, node, 'MonetaryValue')
            self.MonetaryValue = value_
            self.MonetaryValue_nsprefix_ = child_.prefix
# end class InvoiceLineTotalType


class ReturnContractServicesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Code=None, Description=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Code = Code
        self.Code_nsprefix_ = None
        self.Description = Description
        self.Description_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ReturnContractServicesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ReturnContractServicesType.subclass:
            return ReturnContractServicesType.subclass(*args_, **kwargs_)
        else:
            return ReturnContractServicesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Code(self):
        return self.Code
    def set_Code(self, Code):
        self.Code = Code
    def get_Description(self):
        return self.Description
    def set_Description(self, Description):
        self.Description = Description
    def _hasContent(self):
        if (
            self.Code is not None or
            self.Description is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ReturnContractServicesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ReturnContractServicesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ReturnContractServicesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ReturnContractServicesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ReturnContractServicesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ReturnContractServicesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ReturnContractServicesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Code is not None:
            namespaceprefix_ = self.Code_nsprefix_ + ':' if (UseCapturedNS_ and self.Code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCode>%s</%sCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Code), input_name='Code')), namespaceprefix_ , eol_))
        if self.Description is not None:
            namespaceprefix_ = self.Description_nsprefix_ + ':' if (UseCapturedNS_ and self.Description_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDescription>%s</%sDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Description), input_name='Description')), namespaceprefix_ , eol_))
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Code')
            value_ = self.gds_validate_string(value_, node, 'Code')
            self.Code = value_
            self.Code_nsprefix_ = child_.prefix
        elif nodeName_ == 'Description':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Description')
            value_ = self.gds_validate_string(value_, node, 'Description')
            self.Description = value_
            self.Description_nsprefix_ = child_.prefix
# end class ReturnContractServicesType


class TimeInTransitRequest(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Request=None, ShipFrom=None, ShipTo=None, Pickup=None, ShipmentWeight=None, TotalPackagesInShipment=None, InvoiceLineTotal=None, DocumentsOnlyIndicator=None, BillType=None, MaximumListSize=None, SaturdayDeliveryInfoRequestIndicator=None, DropOffAtFacilityIndicator=None, HoldForPickupIndicator=None, IncludeAllServicesIndicator=None, ReturnContractServices=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Request = Request
        self.Request_nsprefix_ = "common"
        self.ShipFrom = ShipFrom
        self.ShipFrom_nsprefix_ = "tnt"
        self.ShipTo = ShipTo
        self.ShipTo_nsprefix_ = "tnt"
        self.Pickup = Pickup
        self.Pickup_nsprefix_ = "tnt"
        self.ShipmentWeight = ShipmentWeight
        self.ShipmentWeight_nsprefix_ = "tnt"
        self.TotalPackagesInShipment = TotalPackagesInShipment
        self.TotalPackagesInShipment_nsprefix_ = None
        self.InvoiceLineTotal = InvoiceLineTotal
        self.InvoiceLineTotal_nsprefix_ = "tnt"
        self.DocumentsOnlyIndicator = DocumentsOnlyIndicator
        self.DocumentsOnlyIndicator_nsprefix_ = None
        self.BillType = BillType
        self.BillType_nsprefix_ = None
        self.MaximumListSize = MaximumListSize
        self.MaximumListSize_nsprefix_ = None
        self.SaturdayDeliveryInfoRequestIndicator = SaturdayDeliveryInfoRequestIndicator
        self.SaturdayDeliveryInfoRequestIndicator_nsprefix_ = None
        self.DropOffAtFacilityIndicator = DropOffAtFacilityIndicator
        self.DropOffAtFacilityIndicator_nsprefix_ = None
        self.HoldForPickupIndicator = HoldForPickupIndicator
        self.HoldForPickupIndicator_nsprefix_ = None
        self.IncludeAllServicesIndicator = IncludeAllServicesIndicator
        self.IncludeAllServicesIndicator_nsprefix_ = None
        if ReturnContractServices is None:
            self.ReturnContractServices = []
        else:
            self.ReturnContractServices = ReturnContractServices
        self.ReturnContractServices_nsprefix_ = "tnt"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TimeInTransitRequest)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TimeInTransitRequest.subclass:
            return TimeInTransitRequest.subclass(*args_, **kwargs_)
        else:
            return TimeInTransitRequest(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Request(self):
        return self.Request
    def set_Request(self, Request):
        self.Request = Request
    def get_ShipFrom(self):
        return self.ShipFrom
    def set_ShipFrom(self, ShipFrom):
        self.ShipFrom = ShipFrom
    def get_ShipTo(self):
        return self.ShipTo
    def set_ShipTo(self, ShipTo):
        self.ShipTo = ShipTo
    def get_Pickup(self):
        return self.Pickup
    def set_Pickup(self, Pickup):
        self.Pickup = Pickup
    def get_ShipmentWeight(self):
        return self.ShipmentWeight
    def set_ShipmentWeight(self, ShipmentWeight):
        self.ShipmentWeight = ShipmentWeight
    def get_TotalPackagesInShipment(self):
        return self.TotalPackagesInShipment
    def set_TotalPackagesInShipment(self, TotalPackagesInShipment):
        self.TotalPackagesInShipment = TotalPackagesInShipment
    def get_InvoiceLineTotal(self):
        return self.InvoiceLineTotal
    def set_InvoiceLineTotal(self, InvoiceLineTotal):
        self.InvoiceLineTotal = InvoiceLineTotal
    def get_DocumentsOnlyIndicator(self):
        return self.DocumentsOnlyIndicator
    def set_DocumentsOnlyIndicator(self, DocumentsOnlyIndicator):
        self.DocumentsOnlyIndicator = DocumentsOnlyIndicator
    def get_BillType(self):
        return self.BillType
    def set_BillType(self, BillType):
        self.BillType = BillType
    def get_MaximumListSize(self):
        return self.MaximumListSize
    def set_MaximumListSize(self, MaximumListSize):
        self.MaximumListSize = MaximumListSize
    def get_SaturdayDeliveryInfoRequestIndicator(self):
        return self.SaturdayDeliveryInfoRequestIndicator
    def set_SaturdayDeliveryInfoRequestIndicator(self, SaturdayDeliveryInfoRequestIndicator):
        self.SaturdayDeliveryInfoRequestIndicator = SaturdayDeliveryInfoRequestIndicator
    def get_DropOffAtFacilityIndicator(self):
        return self.DropOffAtFacilityIndicator
    def set_DropOffAtFacilityIndicator(self, DropOffAtFacilityIndicator):
        self.DropOffAtFacilityIndicator = DropOffAtFacilityIndicator
    def get_HoldForPickupIndicator(self):
        return self.HoldForPickupIndicator
    def set_HoldForPickupIndicator(self, HoldForPickupIndicator):
        self.HoldForPickupIndicator = HoldForPickupIndicator
    def get_IncludeAllServicesIndicator(self):
        return self.IncludeAllServicesIndicator
    def set_IncludeAllServicesIndicator(self, IncludeAllServicesIndicator):
        self.IncludeAllServicesIndicator = IncludeAllServicesIndicator
    def get_ReturnContractServices(self):
        return self.ReturnContractServices
    def set_ReturnContractServices(self, ReturnContractServices):
        self.ReturnContractServices = ReturnContractServices
    def add_ReturnContractServices(self, value):
        self.ReturnContractServices.append(value)
    def insert_ReturnContractServices_at(self, index, value):
        self.ReturnContractServices.insert(index, value)
    def replace_ReturnContractServices_at(self, index, value):
        self.ReturnContractServices[index] = value
    def _hasContent(self):
        if (
            self.Request is not None or
            self.ShipFrom is not None or
            self.ShipTo is not None or
            self.Pickup is not None or
            self.ShipmentWeight is not None or
            self.TotalPackagesInShipment is not None or
            self.InvoiceLineTotal is not None or
            self.DocumentsOnlyIndicator is not None or
            self.BillType is not None or
            self.MaximumListSize is not None or
            self.SaturdayDeliveryInfoRequestIndicator is not None or
            self.DropOffAtFacilityIndicator is not None or
            self.HoldForPickupIndicator is not None or
            self.IncludeAllServicesIndicator is not None or
            self.ReturnContractServices
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TimeInTransitRequest', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TimeInTransitRequest')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TimeInTransitRequest':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TimeInTransitRequest')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TimeInTransitRequest', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TimeInTransitRequest'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TimeInTransitRequest', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Request is not None:
            namespaceprefix_ = self.Request_nsprefix_ + ':' if (UseCapturedNS_ and self.Request_nsprefix_) else ''
            self.Request.export(outfile, level, namespaceprefix_='common:', namespacedef_='', name_='Request', pretty_print=pretty_print)
        if self.ShipFrom is not None:
            namespaceprefix_ = self.ShipFrom_nsprefix_ + ':' if (UseCapturedNS_ and self.ShipFrom_nsprefix_) else ''
            self.ShipFrom.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ShipFrom', pretty_print=pretty_print)
        if self.ShipTo is not None:
            namespaceprefix_ = self.ShipTo_nsprefix_ + ':' if (UseCapturedNS_ and self.ShipTo_nsprefix_) else ''
            self.ShipTo.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ShipTo', pretty_print=pretty_print)
        if self.Pickup is not None:
            namespaceprefix_ = self.Pickup_nsprefix_ + ':' if (UseCapturedNS_ and self.Pickup_nsprefix_) else ''
            self.Pickup.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Pickup', pretty_print=pretty_print)
        if self.ShipmentWeight is not None:
            namespaceprefix_ = self.ShipmentWeight_nsprefix_ + ':' if (UseCapturedNS_ and self.ShipmentWeight_nsprefix_) else ''
            self.ShipmentWeight.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ShipmentWeight', pretty_print=pretty_print)
        if self.TotalPackagesInShipment is not None:
            namespaceprefix_ = self.TotalPackagesInShipment_nsprefix_ + ':' if (UseCapturedNS_ and self.TotalPackagesInShipment_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTotalPackagesInShipment>%s</%sTotalPackagesInShipment>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TotalPackagesInShipment), input_name='TotalPackagesInShipment')), namespaceprefix_ , eol_))
        if self.InvoiceLineTotal is not None:
            namespaceprefix_ = self.InvoiceLineTotal_nsprefix_ + ':' if (UseCapturedNS_ and self.InvoiceLineTotal_nsprefix_) else ''
            self.InvoiceLineTotal.export(outfile, level, namespaceprefix_, namespacedef_='', name_='InvoiceLineTotal', pretty_print=pretty_print)
        if self.DocumentsOnlyIndicator is not None:
            namespaceprefix_ = self.DocumentsOnlyIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.DocumentsOnlyIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDocumentsOnlyIndicator>%s</%sDocumentsOnlyIndicator>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.DocumentsOnlyIndicator), input_name='DocumentsOnlyIndicator')), namespaceprefix_ , eol_))
        if self.BillType is not None:
            namespaceprefix_ = self.BillType_nsprefix_ + ':' if (UseCapturedNS_ and self.BillType_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBillType>%s</%sBillType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.BillType), input_name='BillType')), namespaceprefix_ , eol_))
        if self.MaximumListSize is not None:
            namespaceprefix_ = self.MaximumListSize_nsprefix_ + ':' if (UseCapturedNS_ and self.MaximumListSize_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMaximumListSize>%s</%sMaximumListSize>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.MaximumListSize), input_name='MaximumListSize')), namespaceprefix_ , eol_))
        if self.SaturdayDeliveryInfoRequestIndicator is not None:
            namespaceprefix_ = self.SaturdayDeliveryInfoRequestIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.SaturdayDeliveryInfoRequestIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSaturdayDeliveryInfoRequestIndicator>%s</%sSaturdayDeliveryInfoRequestIndicator>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SaturdayDeliveryInfoRequestIndicator), input_name='SaturdayDeliveryInfoRequestIndicator')), namespaceprefix_ , eol_))
        if self.DropOffAtFacilityIndicator is not None:
            namespaceprefix_ = self.DropOffAtFacilityIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.DropOffAtFacilityIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDropOffAtFacilityIndicator>%s</%sDropOffAtFacilityIndicator>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.DropOffAtFacilityIndicator), input_name='DropOffAtFacilityIndicator')), namespaceprefix_ , eol_))
        if self.HoldForPickupIndicator is not None:
            namespaceprefix_ = self.HoldForPickupIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.HoldForPickupIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sHoldForPickupIndicator>%s</%sHoldForPickupIndicator>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.HoldForPickupIndicator), input_name='HoldForPickupIndicator')), namespaceprefix_ , eol_))
        if self.IncludeAllServicesIndicator is not None:
            namespaceprefix_ = self.IncludeAllServicesIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.IncludeAllServicesIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sIncludeAllServicesIndicator>%s</%sIncludeAllServicesIndicator>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.IncludeAllServicesIndicator), input_name='IncludeAllServicesIndicator')), namespaceprefix_ , eol_))
        for ReturnContractServices_ in self.ReturnContractServices:
            namespaceprefix_ = self.ReturnContractServices_nsprefix_ + ':' if (UseCapturedNS_ and self.ReturnContractServices_nsprefix_) else ''
            ReturnContractServices_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ReturnContractServices', pretty_print=pretty_print)
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Request':
            obj_ = RequestType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Request = obj_
            obj_.original_tagname_ = 'Request'
        elif nodeName_ == 'ShipFrom':
            obj_ = RequestShipFromType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ShipFrom = obj_
            obj_.original_tagname_ = 'ShipFrom'
        elif nodeName_ == 'ShipTo':
            obj_ = RequestShipToType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ShipTo = obj_
            obj_.original_tagname_ = 'ShipTo'
        elif nodeName_ == 'Pickup':
            obj_ = PickupType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Pickup = obj_
            obj_.original_tagname_ = 'Pickup'
        elif nodeName_ == 'ShipmentWeight':
            obj_ = ShipmentWeightType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ShipmentWeight = obj_
            obj_.original_tagname_ = 'ShipmentWeight'
        elif nodeName_ == 'TotalPackagesInShipment':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TotalPackagesInShipment')
            value_ = self.gds_validate_string(value_, node, 'TotalPackagesInShipment')
            self.TotalPackagesInShipment = value_
            self.TotalPackagesInShipment_nsprefix_ = child_.prefix
        elif nodeName_ == 'InvoiceLineTotal':
            obj_ = InvoiceLineTotalType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.InvoiceLineTotal = obj_
            obj_.original_tagname_ = 'InvoiceLineTotal'
        elif nodeName_ == 'DocumentsOnlyIndicator':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'DocumentsOnlyIndicator')
            value_ = self.gds_validate_string(value_, node, 'DocumentsOnlyIndicator')
            self.DocumentsOnlyIndicator = value_
            self.DocumentsOnlyIndicator_nsprefix_ = child_.prefix
        elif nodeName_ == 'BillType':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'BillType')
            value_ = self.gds_validate_string(value_, node, 'BillType')
            self.BillType = value_
            self.BillType_nsprefix_ = child_.prefix
        elif nodeName_ == 'MaximumListSize':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'MaximumListSize')
            value_ = self.gds_validate_string(value_, node, 'MaximumListSize')
            self.MaximumListSize = value_
            self.MaximumListSize_nsprefix_ = child_.prefix
        elif nodeName_ == 'SaturdayDeliveryInfoRequestIndicator':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SaturdayDeliveryInfoRequestIndicator')
            value_ = self.gds_validate_string(value_, node, 'SaturdayDeliveryInfoRequestIndicator')
            self.SaturdayDeliveryInfoRequestIndicator = value_
            self.SaturdayDeliveryInfoRequestIndicator_nsprefix_ = child_.prefix
        elif nodeName_ == 'DropOffAtFacilityIndicator':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'DropOffAtFacilityIndicator')
            value_ = self.gds_validate_string(value_, node, 'DropOffAtFacilityIndicator')
            self.DropOffAtFacilityIndicator = value_
            self.DropOffAtFacilityIndicator_nsprefix_ = child_.prefix
        elif nodeName_ == 'HoldForPickupIndicator':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'HoldForPickupIndicator')
            value_ = self.gds_validate_string(value_, node, 'HoldForPickupIndicator')
            self.HoldForPickupIndicator = value_
            self.HoldForPickupIndicator_nsprefix_ = child_.prefix
        elif nodeName_ == 'IncludeAllServicesIndicator':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'IncludeAllServicesIndicator')
            value_ = self.gds_validate_string(value_, node, 'IncludeAllServicesIndicator')
            self.IncludeAllServicesIndicator = value_
            self.IncludeAllServicesIndicator_nsprefix_ = child_.prefix
        elif nodeName_ == 'ReturnContractServices':
            obj_ = ReturnContractServicesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ReturnContractServices.append(obj_)
            obj_.original_tagname_ = 'ReturnContractServices'
# end class TimeInTransitRequest


class EstimatedArrivalType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Arrival=None, BusinessDaysInTransit=None, Pickup=None, DayOfWeek=None, CustomerCenterCutoff=None, DelayCount=None, HolidayCount=None, RestDays=None, TotalTransitDays=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Arrival = Arrival
        self.Arrival_nsprefix_ = "tnt"
        self.BusinessDaysInTransit = BusinessDaysInTransit
        self.BusinessDaysInTransit_nsprefix_ = None
        self.Pickup = Pickup
        self.Pickup_nsprefix_ = "tnt"
        self.DayOfWeek = DayOfWeek
        self.DayOfWeek_nsprefix_ = None
        self.CustomerCenterCutoff = CustomerCenterCutoff
        self.CustomerCenterCutoff_nsprefix_ = None
        self.DelayCount = DelayCount
        self.DelayCount_nsprefix_ = None
        self.HolidayCount = HolidayCount
        self.HolidayCount_nsprefix_ = None
        self.RestDays = RestDays
        self.RestDays_nsprefix_ = None
        self.TotalTransitDays = TotalTransitDays
        self.TotalTransitDays_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, EstimatedArrivalType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if EstimatedArrivalType.subclass:
            return EstimatedArrivalType.subclass(*args_, **kwargs_)
        else:
            return EstimatedArrivalType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Arrival(self):
        return self.Arrival
    def set_Arrival(self, Arrival):
        self.Arrival = Arrival
    def get_BusinessDaysInTransit(self):
        return self.BusinessDaysInTransit
    def set_BusinessDaysInTransit(self, BusinessDaysInTransit):
        self.BusinessDaysInTransit = BusinessDaysInTransit
    def get_Pickup(self):
        return self.Pickup
    def set_Pickup(self, Pickup):
        self.Pickup = Pickup
    def get_DayOfWeek(self):
        return self.DayOfWeek
    def set_DayOfWeek(self, DayOfWeek):
        self.DayOfWeek = DayOfWeek
    def get_CustomerCenterCutoff(self):
        return self.CustomerCenterCutoff
    def set_CustomerCenterCutoff(self, CustomerCenterCutoff):
        self.CustomerCenterCutoff = CustomerCenterCutoff
    def get_DelayCount(self):
        return self.DelayCount
    def set_DelayCount(self, DelayCount):
        self.DelayCount = DelayCount
    def get_HolidayCount(self):
        return self.HolidayCount
    def set_HolidayCount(self, HolidayCount):
        self.HolidayCount = HolidayCount
    def get_RestDays(self):
        return self.RestDays
    def set_RestDays(self, RestDays):
        self.RestDays = RestDays
    def get_TotalTransitDays(self):
        return self.TotalTransitDays
    def set_TotalTransitDays(self, TotalTransitDays):
        self.TotalTransitDays = TotalTransitDays
    def _hasContent(self):
        if (
            self.Arrival is not None or
            self.BusinessDaysInTransit is not None or
            self.Pickup is not None or
            self.DayOfWeek is not None or
            self.CustomerCenterCutoff is not None or
            self.DelayCount is not None or
            self.HolidayCount is not None or
            self.RestDays is not None or
            self.TotalTransitDays is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='EstimatedArrivalType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('EstimatedArrivalType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'EstimatedArrivalType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='EstimatedArrivalType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='EstimatedArrivalType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='EstimatedArrivalType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='EstimatedArrivalType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Arrival is not None:
            namespaceprefix_ = self.Arrival_nsprefix_ + ':' if (UseCapturedNS_ and self.Arrival_nsprefix_) else ''
            self.Arrival.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Arrival', pretty_print=pretty_print)
        if self.BusinessDaysInTransit is not None:
            namespaceprefix_ = self.BusinessDaysInTransit_nsprefix_ + ':' if (UseCapturedNS_ and self.BusinessDaysInTransit_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBusinessDaysInTransit>%s</%sBusinessDaysInTransit>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.BusinessDaysInTransit), input_name='BusinessDaysInTransit')), namespaceprefix_ , eol_))
        if self.Pickup is not None:
            namespaceprefix_ = self.Pickup_nsprefix_ + ':' if (UseCapturedNS_ and self.Pickup_nsprefix_) else ''
            self.Pickup.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Pickup', pretty_print=pretty_print)
        if self.DayOfWeek is not None:
            namespaceprefix_ = self.DayOfWeek_nsprefix_ + ':' if (UseCapturedNS_ and self.DayOfWeek_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDayOfWeek>%s</%sDayOfWeek>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.DayOfWeek), input_name='DayOfWeek')), namespaceprefix_ , eol_))
        if self.CustomerCenterCutoff is not None:
            namespaceprefix_ = self.CustomerCenterCutoff_nsprefix_ + ':' if (UseCapturedNS_ and self.CustomerCenterCutoff_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCustomerCenterCutoff>%s</%sCustomerCenterCutoff>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CustomerCenterCutoff), input_name='CustomerCenterCutoff')), namespaceprefix_ , eol_))
        if self.DelayCount is not None:
            namespaceprefix_ = self.DelayCount_nsprefix_ + ':' if (UseCapturedNS_ and self.DelayCount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDelayCount>%s</%sDelayCount>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.DelayCount), input_name='DelayCount')), namespaceprefix_ , eol_))
        if self.HolidayCount is not None:
            namespaceprefix_ = self.HolidayCount_nsprefix_ + ':' if (UseCapturedNS_ and self.HolidayCount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sHolidayCount>%s</%sHolidayCount>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.HolidayCount), input_name='HolidayCount')), namespaceprefix_ , eol_))
        if self.RestDays is not None:
            namespaceprefix_ = self.RestDays_nsprefix_ + ':' if (UseCapturedNS_ and self.RestDays_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRestDays>%s</%sRestDays>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.RestDays), input_name='RestDays')), namespaceprefix_ , eol_))
        if self.TotalTransitDays is not None:
            namespaceprefix_ = self.TotalTransitDays_nsprefix_ + ':' if (UseCapturedNS_ and self.TotalTransitDays_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTotalTransitDays>%s</%sTotalTransitDays>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TotalTransitDays), input_name='TotalTransitDays')), namespaceprefix_ , eol_))
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Arrival':
            obj_ = PickupType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Arrival = obj_
            obj_.original_tagname_ = 'Arrival'
        elif nodeName_ == 'BusinessDaysInTransit':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'BusinessDaysInTransit')
            value_ = self.gds_validate_string(value_, node, 'BusinessDaysInTransit')
            self.BusinessDaysInTransit = value_
            self.BusinessDaysInTransit_nsprefix_ = child_.prefix
        elif nodeName_ == 'Pickup':
            obj_ = PickupType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Pickup = obj_
            obj_.original_tagname_ = 'Pickup'
        elif nodeName_ == 'DayOfWeek':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'DayOfWeek')
            value_ = self.gds_validate_string(value_, node, 'DayOfWeek')
            self.DayOfWeek = value_
            self.DayOfWeek_nsprefix_ = child_.prefix
        elif nodeName_ == 'CustomerCenterCutoff':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CustomerCenterCutoff')
            value_ = self.gds_validate_string(value_, node, 'CustomerCenterCutoff')
            self.CustomerCenterCutoff = value_
            self.CustomerCenterCutoff_nsprefix_ = child_.prefix
        elif nodeName_ == 'DelayCount':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'DelayCount')
            value_ = self.gds_validate_string(value_, node, 'DelayCount')
            self.DelayCount = value_
            self.DelayCount_nsprefix_ = child_.prefix
        elif nodeName_ == 'HolidayCount':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'HolidayCount')
            value_ = self.gds_validate_string(value_, node, 'HolidayCount')
            self.HolidayCount = value_
            self.HolidayCount_nsprefix_ = child_.prefix
        elif nodeName_ == 'RestDays':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'RestDays')
            value_ = self.gds_validate_string(value_, node, 'RestDays')
            self.RestDays = value_
            self.RestDays_nsprefix_ = child_.prefix
        elif nodeName_ == 'TotalTransitDays':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TotalTransitDays')
            value_ = self.gds_validate_string(value_, node, 'TotalTransitDays')
            self.TotalTransitDays = value_
            self.TotalTransitDays_nsprefix_ = child_.prefix
# end class EstimatedArrivalType


class ServiceSummaryType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Service=None, GuaranteedIndicator=None, Disclaimer=None, EstimatedArrival=None, SaturdayDelivery=None, SaturdayDeliveryDisclaimer=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Service = Service
        self.Service_nsprefix_ = None
        self.GuaranteedIndicator = GuaranteedIndicator
        self.GuaranteedIndicator_nsprefix_ = None
        self.Disclaimer = Disclaimer
        self.Disclaimer_nsprefix_ = None
        self.EstimatedArrival = EstimatedArrival
        self.EstimatedArrival_nsprefix_ = "tnt"
        self.SaturdayDelivery = SaturdayDelivery
        self.SaturdayDelivery_nsprefix_ = None
        self.SaturdayDeliveryDisclaimer = SaturdayDeliveryDisclaimer
        self.SaturdayDeliveryDisclaimer_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ServiceSummaryType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ServiceSummaryType.subclass:
            return ServiceSummaryType.subclass(*args_, **kwargs_)
        else:
            return ServiceSummaryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Service(self):
        return self.Service
    def set_Service(self, Service):
        self.Service = Service
    def get_GuaranteedIndicator(self):
        return self.GuaranteedIndicator
    def set_GuaranteedIndicator(self, GuaranteedIndicator):
        self.GuaranteedIndicator = GuaranteedIndicator
    def get_Disclaimer(self):
        return self.Disclaimer
    def set_Disclaimer(self, Disclaimer):
        self.Disclaimer = Disclaimer
    def get_EstimatedArrival(self):
        return self.EstimatedArrival
    def set_EstimatedArrival(self, EstimatedArrival):
        self.EstimatedArrival = EstimatedArrival
    def get_SaturdayDelivery(self):
        return self.SaturdayDelivery
    def set_SaturdayDelivery(self, SaturdayDelivery):
        self.SaturdayDelivery = SaturdayDelivery
    def get_SaturdayDeliveryDisclaimer(self):
        return self.SaturdayDeliveryDisclaimer
    def set_SaturdayDeliveryDisclaimer(self, SaturdayDeliveryDisclaimer):
        self.SaturdayDeliveryDisclaimer = SaturdayDeliveryDisclaimer
    def _hasContent(self):
        if (
            self.Service is not None or
            self.GuaranteedIndicator is not None or
            self.Disclaimer is not None or
            self.EstimatedArrival is not None or
            self.SaturdayDelivery is not None or
            self.SaturdayDeliveryDisclaimer is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ServiceSummaryType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ServiceSummaryType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ServiceSummaryType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ServiceSummaryType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ServiceSummaryType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ServiceSummaryType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ServiceSummaryType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Service is not None:
            namespaceprefix_ = self.Service_nsprefix_ + ':' if (UseCapturedNS_ and self.Service_nsprefix_) else ''
            self.Service.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Service', pretty_print=pretty_print)
        if self.GuaranteedIndicator is not None:
            namespaceprefix_ = self.GuaranteedIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.GuaranteedIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sGuaranteedIndicator>%s</%sGuaranteedIndicator>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.GuaranteedIndicator), input_name='GuaranteedIndicator')), namespaceprefix_ , eol_))
        if self.Disclaimer is not None:
            namespaceprefix_ = self.Disclaimer_nsprefix_ + ':' if (UseCapturedNS_ and self.Disclaimer_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDisclaimer>%s</%sDisclaimer>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Disclaimer), input_name='Disclaimer')), namespaceprefix_ , eol_))
        if self.EstimatedArrival is not None:
            namespaceprefix_ = self.EstimatedArrival_nsprefix_ + ':' if (UseCapturedNS_ and self.EstimatedArrival_nsprefix_) else ''
            self.EstimatedArrival.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EstimatedArrival', pretty_print=pretty_print)
        if self.SaturdayDelivery is not None:
            namespaceprefix_ = self.SaturdayDelivery_nsprefix_ + ':' if (UseCapturedNS_ and self.SaturdayDelivery_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSaturdayDelivery>%s</%sSaturdayDelivery>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SaturdayDelivery), input_name='SaturdayDelivery')), namespaceprefix_ , eol_))
        if self.SaturdayDeliveryDisclaimer is not None:
            namespaceprefix_ = self.SaturdayDeliveryDisclaimer_nsprefix_ + ':' if (UseCapturedNS_ and self.SaturdayDeliveryDisclaimer_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSaturdayDeliveryDisclaimer>%s</%sSaturdayDeliveryDisclaimer>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SaturdayDeliveryDisclaimer), input_name='SaturdayDeliveryDisclaimer')), namespaceprefix_ , eol_))
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Service':
            obj_ = CodeDescriptionType1.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Service = obj_
            obj_.original_tagname_ = 'Service'
        elif nodeName_ == 'GuaranteedIndicator':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'GuaranteedIndicator')
            value_ = self.gds_validate_string(value_, node, 'GuaranteedIndicator')
            self.GuaranteedIndicator = value_
            self.GuaranteedIndicator_nsprefix_ = child_.prefix
        elif nodeName_ == 'Disclaimer':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Disclaimer')
            value_ = self.gds_validate_string(value_, node, 'Disclaimer')
            self.Disclaimer = value_
            self.Disclaimer_nsprefix_ = child_.prefix
        elif nodeName_ == 'EstimatedArrival':
            obj_ = EstimatedArrivalType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EstimatedArrival = obj_
            obj_.original_tagname_ = 'EstimatedArrival'
        elif nodeName_ == 'SaturdayDelivery':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SaturdayDelivery')
            value_ = self.gds_validate_string(value_, node, 'SaturdayDelivery')
            self.SaturdayDelivery = value_
            self.SaturdayDelivery_nsprefix_ = child_.prefix
        elif nodeName_ == 'SaturdayDeliveryDisclaimer':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SaturdayDeliveryDisclaimer')
            value_ = self.gds_validate_string(value_, node, 'SaturdayDeliveryDisclaimer')
            self.SaturdayDeliveryDisclaimer = value_
            self.SaturdayDeliveryDisclaimer_nsprefix_ = child_.prefix
# end class ServiceSummaryType


class TransitResponseType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ShipFrom=None, ShipTo=None, PickupDate=None, ShipmentWeight=None, InvoiceLineTotal=None, DocumentsOnlyIndicator=None, BillType=None, MaximumListSize=None, ServiceSummary=None, AutoDutyCode=None, Disclaimer=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ShipFrom = ShipFrom
        self.ShipFrom_nsprefix_ = "tnt"
        self.ShipTo = ShipTo
        self.ShipTo_nsprefix_ = "tnt"
        self.PickupDate = PickupDate
        self.PickupDate_nsprefix_ = None
        self.ShipmentWeight = ShipmentWeight
        self.ShipmentWeight_nsprefix_ = "tnt"
        self.InvoiceLineTotal = InvoiceLineTotal
        self.InvoiceLineTotal_nsprefix_ = "tnt"
        self.DocumentsOnlyIndicator = DocumentsOnlyIndicator
        self.DocumentsOnlyIndicator_nsprefix_ = None
        self.BillType = BillType
        self.BillType_nsprefix_ = None
        self.MaximumListSize = MaximumListSize
        self.MaximumListSize_nsprefix_ = None
        if ServiceSummary is None:
            self.ServiceSummary = []
        else:
            self.ServiceSummary = ServiceSummary
        self.ServiceSummary_nsprefix_ = "tnt"
        self.AutoDutyCode = AutoDutyCode
        self.AutoDutyCode_nsprefix_ = None
        self.Disclaimer = Disclaimer
        self.Disclaimer_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TransitResponseType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TransitResponseType.subclass:
            return TransitResponseType.subclass(*args_, **kwargs_)
        else:
            return TransitResponseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ShipFrom(self):
        return self.ShipFrom
    def set_ShipFrom(self, ShipFrom):
        self.ShipFrom = ShipFrom
    def get_ShipTo(self):
        return self.ShipTo
    def set_ShipTo(self, ShipTo):
        self.ShipTo = ShipTo
    def get_PickupDate(self):
        return self.PickupDate
    def set_PickupDate(self, PickupDate):
        self.PickupDate = PickupDate
    def get_ShipmentWeight(self):
        return self.ShipmentWeight
    def set_ShipmentWeight(self, ShipmentWeight):
        self.ShipmentWeight = ShipmentWeight
    def get_InvoiceLineTotal(self):
        return self.InvoiceLineTotal
    def set_InvoiceLineTotal(self, InvoiceLineTotal):
        self.InvoiceLineTotal = InvoiceLineTotal
    def get_DocumentsOnlyIndicator(self):
        return self.DocumentsOnlyIndicator
    def set_DocumentsOnlyIndicator(self, DocumentsOnlyIndicator):
        self.DocumentsOnlyIndicator = DocumentsOnlyIndicator
    def get_BillType(self):
        return self.BillType
    def set_BillType(self, BillType):
        self.BillType = BillType
    def get_MaximumListSize(self):
        return self.MaximumListSize
    def set_MaximumListSize(self, MaximumListSize):
        self.MaximumListSize = MaximumListSize
    def get_ServiceSummary(self):
        return self.ServiceSummary
    def set_ServiceSummary(self, ServiceSummary):
        self.ServiceSummary = ServiceSummary
    def add_ServiceSummary(self, value):
        self.ServiceSummary.append(value)
    def insert_ServiceSummary_at(self, index, value):
        self.ServiceSummary.insert(index, value)
    def replace_ServiceSummary_at(self, index, value):
        self.ServiceSummary[index] = value
    def get_AutoDutyCode(self):
        return self.AutoDutyCode
    def set_AutoDutyCode(self, AutoDutyCode):
        self.AutoDutyCode = AutoDutyCode
    def get_Disclaimer(self):
        return self.Disclaimer
    def set_Disclaimer(self, Disclaimer):
        self.Disclaimer = Disclaimer
    def _hasContent(self):
        if (
            self.ShipFrom is not None or
            self.ShipTo is not None or
            self.PickupDate is not None or
            self.ShipmentWeight is not None or
            self.InvoiceLineTotal is not None or
            self.DocumentsOnlyIndicator is not None or
            self.BillType is not None or
            self.MaximumListSize is not None or
            self.ServiceSummary or
            self.AutoDutyCode is not None or
            self.Disclaimer is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TransitResponseType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TransitResponseType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TransitResponseType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TransitResponseType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TransitResponseType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TransitResponseType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TransitResponseType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ShipFrom is not None:
            namespaceprefix_ = self.ShipFrom_nsprefix_ + ':' if (UseCapturedNS_ and self.ShipFrom_nsprefix_) else ''
            self.ShipFrom.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ShipFrom', pretty_print=pretty_print)
        if self.ShipTo is not None:
            namespaceprefix_ = self.ShipTo_nsprefix_ + ':' if (UseCapturedNS_ and self.ShipTo_nsprefix_) else ''
            self.ShipTo.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ShipTo', pretty_print=pretty_print)
        if self.PickupDate is not None:
            namespaceprefix_ = self.PickupDate_nsprefix_ + ':' if (UseCapturedNS_ and self.PickupDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPickupDate>%s</%sPickupDate>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.PickupDate), input_name='PickupDate')), namespaceprefix_ , eol_))
        if self.ShipmentWeight is not None:
            namespaceprefix_ = self.ShipmentWeight_nsprefix_ + ':' if (UseCapturedNS_ and self.ShipmentWeight_nsprefix_) else ''
            self.ShipmentWeight.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ShipmentWeight', pretty_print=pretty_print)
        if self.InvoiceLineTotal is not None:
            namespaceprefix_ = self.InvoiceLineTotal_nsprefix_ + ':' if (UseCapturedNS_ and self.InvoiceLineTotal_nsprefix_) else ''
            self.InvoiceLineTotal.export(outfile, level, namespaceprefix_, namespacedef_='', name_='InvoiceLineTotal', pretty_print=pretty_print)
        if self.DocumentsOnlyIndicator is not None:
            namespaceprefix_ = self.DocumentsOnlyIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.DocumentsOnlyIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDocumentsOnlyIndicator>%s</%sDocumentsOnlyIndicator>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.DocumentsOnlyIndicator), input_name='DocumentsOnlyIndicator')), namespaceprefix_ , eol_))
        if self.BillType is not None:
            namespaceprefix_ = self.BillType_nsprefix_ + ':' if (UseCapturedNS_ and self.BillType_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBillType>%s</%sBillType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.BillType), input_name='BillType')), namespaceprefix_ , eol_))
        if self.MaximumListSize is not None:
            namespaceprefix_ = self.MaximumListSize_nsprefix_ + ':' if (UseCapturedNS_ and self.MaximumListSize_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMaximumListSize>%s</%sMaximumListSize>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.MaximumListSize), input_name='MaximumListSize')), namespaceprefix_ , eol_))
        for ServiceSummary_ in self.ServiceSummary:
            namespaceprefix_ = self.ServiceSummary_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceSummary_nsprefix_) else ''
            ServiceSummary_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ServiceSummary', pretty_print=pretty_print)
        if self.AutoDutyCode is not None:
            namespaceprefix_ = self.AutoDutyCode_nsprefix_ + ':' if (UseCapturedNS_ and self.AutoDutyCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAutoDutyCode>%s</%sAutoDutyCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.AutoDutyCode), input_name='AutoDutyCode')), namespaceprefix_ , eol_))
        if self.Disclaimer is not None:
            namespaceprefix_ = self.Disclaimer_nsprefix_ + ':' if (UseCapturedNS_ and self.Disclaimer_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDisclaimer>%s</%sDisclaimer>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Disclaimer), input_name='Disclaimer')), namespaceprefix_ , eol_))
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ShipFrom':
            obj_ = ResponseShipFromType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ShipFrom = obj_
            obj_.original_tagname_ = 'ShipFrom'
        elif nodeName_ == 'ShipTo':
            obj_ = ResponseShipToType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ShipTo = obj_
            obj_.original_tagname_ = 'ShipTo'
        elif nodeName_ == 'PickupDate':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'PickupDate')
            value_ = self.gds_validate_string(value_, node, 'PickupDate')
            self.PickupDate = value_
            self.PickupDate_nsprefix_ = child_.prefix
        elif nodeName_ == 'ShipmentWeight':
            obj_ = ShipmentWeightType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ShipmentWeight = obj_
            obj_.original_tagname_ = 'ShipmentWeight'
        elif nodeName_ == 'InvoiceLineTotal':
            obj_ = InvoiceLineTotalType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.InvoiceLineTotal = obj_
            obj_.original_tagname_ = 'InvoiceLineTotal'
        elif nodeName_ == 'DocumentsOnlyIndicator':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'DocumentsOnlyIndicator')
            value_ = self.gds_validate_string(value_, node, 'DocumentsOnlyIndicator')
            self.DocumentsOnlyIndicator = value_
            self.DocumentsOnlyIndicator_nsprefix_ = child_.prefix
        elif nodeName_ == 'BillType':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'BillType')
            value_ = self.gds_validate_string(value_, node, 'BillType')
            self.BillType = value_
            self.BillType_nsprefix_ = child_.prefix
        elif nodeName_ == 'MaximumListSize':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'MaximumListSize')
            value_ = self.gds_validate_string(value_, node, 'MaximumListSize')
            self.MaximumListSize = value_
            self.MaximumListSize_nsprefix_ = child_.prefix
        elif nodeName_ == 'ServiceSummary':
            obj_ = ServiceSummaryType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ServiceSummary.append(obj_)
            obj_.original_tagname_ = 'ServiceSummary'
        elif nodeName_ == 'AutoDutyCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'AutoDutyCode')
            value_ = self.gds_validate_string(value_, node, 'AutoDutyCode')
            self.AutoDutyCode = value_
            self.AutoDutyCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'Disclaimer':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Disclaimer')
            value_ = self.gds_validate_string(value_, node, 'Disclaimer')
            self.Disclaimer = value_
            self.Disclaimer_nsprefix_ = child_.prefix
# end class TransitResponseType


class CandidateType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Address=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Address = Address
        self.Address_nsprefix_ = "tnt"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CandidateType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CandidateType.subclass:
            return CandidateType.subclass(*args_, **kwargs_)
        else:
            return CandidateType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Address(self):
        return self.Address
    def set_Address(self, Address):
        self.Address = Address
    def _hasContent(self):
        if (
            self.Address is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CandidateType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CandidateType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CandidateType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CandidateType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CandidateType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CandidateType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CandidateType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Address is not None:
            namespaceprefix_ = self.Address_nsprefix_ + ':' if (UseCapturedNS_ and self.Address_nsprefix_) else ''
            self.Address.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Address', pretty_print=pretty_print)
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Address':
            obj_ = ResponseShipListAddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Address = obj_
            obj_.original_tagname_ = 'Address'
# end class CandidateType


class ShipListType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Candidate=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Candidate is None:
            self.Candidate = []
        else:
            self.Candidate = Candidate
        self.Candidate_nsprefix_ = "tnt"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ShipListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ShipListType.subclass:
            return ShipListType.subclass(*args_, **kwargs_)
        else:
            return ShipListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Candidate(self):
        return self.Candidate
    def set_Candidate(self, Candidate):
        self.Candidate = Candidate
    def add_Candidate(self, value):
        self.Candidate.append(value)
    def insert_Candidate_at(self, index, value):
        self.Candidate.insert(index, value)
    def replace_Candidate_at(self, index, value):
        self.Candidate[index] = value
    def _hasContent(self):
        if (
            self.Candidate
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ShipListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ShipListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ShipListType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ShipListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ShipListType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Candidate_ in self.Candidate:
            namespaceprefix_ = self.Candidate_nsprefix_ + ':' if (UseCapturedNS_ and self.Candidate_nsprefix_) else ''
            Candidate_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Candidate', pretty_print=pretty_print)
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Candidate':
            obj_ = CandidateType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Candidate.append(obj_)
            obj_.original_tagname_ = 'Candidate'
# end class ShipListType


class CandidateResponseType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ShipFromList=None, ShipToList=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ShipFromList = ShipFromList
        self.ShipFromList_nsprefix_ = "tnt"
        self.ShipToList = ShipToList
        self.ShipToList_nsprefix_ = "tnt"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CandidateResponseType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CandidateResponseType.subclass:
            return CandidateResponseType.subclass(*args_, **kwargs_)
        else:
            return CandidateResponseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ShipFromList(self):
        return self.ShipFromList
    def set_ShipFromList(self, ShipFromList):
        self.ShipFromList = ShipFromList
    def get_ShipToList(self):
        return self.ShipToList
    def set_ShipToList(self, ShipToList):
        self.ShipToList = ShipToList
    def _hasContent(self):
        if (
            self.ShipFromList is not None or
            self.ShipToList is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CandidateResponseType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CandidateResponseType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CandidateResponseType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CandidateResponseType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CandidateResponseType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CandidateResponseType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CandidateResponseType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ShipFromList is not None:
            namespaceprefix_ = self.ShipFromList_nsprefix_ + ':' if (UseCapturedNS_ and self.ShipFromList_nsprefix_) else ''
            self.ShipFromList.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ShipFromList', pretty_print=pretty_print)
        if self.ShipToList is not None:
            namespaceprefix_ = self.ShipToList_nsprefix_ + ':' if (UseCapturedNS_ and self.ShipToList_nsprefix_) else ''
            self.ShipToList.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ShipToList', pretty_print=pretty_print)
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ShipFromList':
            obj_ = ShipListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ShipFromList = obj_
            obj_.original_tagname_ = 'ShipFromList'
        elif nodeName_ == 'ShipToList':
            obj_ = ShipListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ShipToList = obj_
            obj_.original_tagname_ = 'ShipToList'
# end class CandidateResponseType


class TimeInTransitResponse(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Response=None, TransitResponse=None, CandidateResponse=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Response = Response
        self.Response_nsprefix_ = "common"
        self.TransitResponse = TransitResponse
        self.TransitResponse_nsprefix_ = "tnt"
        self.CandidateResponse = CandidateResponse
        self.CandidateResponse_nsprefix_ = "tnt"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TimeInTransitResponse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TimeInTransitResponse.subclass:
            return TimeInTransitResponse.subclass(*args_, **kwargs_)
        else:
            return TimeInTransitResponse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Response(self):
        return self.Response
    def set_Response(self, Response):
        self.Response = Response
    def get_TransitResponse(self):
        return self.TransitResponse
    def set_TransitResponse(self, TransitResponse):
        self.TransitResponse = TransitResponse
    def get_CandidateResponse(self):
        return self.CandidateResponse
    def set_CandidateResponse(self, CandidateResponse):
        self.CandidateResponse = CandidateResponse
    def _hasContent(self):
        if (
            self.Response is not None or
            self.TransitResponse is not None or
            self.CandidateResponse is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TimeInTransitResponse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TimeInTransitResponse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TimeInTransitResponse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TimeInTransitResponse')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TimeInTransitResponse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TimeInTransitResponse'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TimeInTransitResponse', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Response is not None:
            namespaceprefix_ = self.Response_nsprefix_ + ':' if (UseCapturedNS_ and self.Response_nsprefix_) else ''
            self.Response.export(outfile, level, namespaceprefix_='common:', namespacedef_='', name_='Response', pretty_print=pretty_print)
        if self.TransitResponse is not None:
            namespaceprefix_ = self.TransitResponse_nsprefix_ + ':' if (UseCapturedNS_ and self.TransitResponse_nsprefix_) else ''
            self.TransitResponse.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TransitResponse', pretty_print=pretty_print)
        if self.CandidateResponse is not None:
            namespaceprefix_ = self.CandidateResponse_nsprefix_ + ':' if (UseCapturedNS_ and self.CandidateResponse_nsprefix_) else ''
            self.CandidateResponse.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CandidateResponse', pretty_print=pretty_print)
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Response':
            obj_ = ResponseType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Response = obj_
            obj_.original_tagname_ = 'Response'
        elif nodeName_ == 'TransitResponse':
            obj_ = TransitResponseType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TransitResponse = obj_
            obj_.original_tagname_ = 'TransitResponse'
        elif nodeName_ == 'CandidateResponse':
            obj_ = CandidateResponseType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CandidateResponse = obj_
            obj_.original_tagname_ = 'CandidateResponse'
# end class TimeInTransitResponse


class ClientInformationType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Property=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Property is None:
            self.Property = []
        else:
            self.Property = Property
        self.Property_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ClientInformationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ClientInformationType.subclass:
            return ClientInformationType.subclass(*args_, **kwargs_)
        else:
            return ClientInformationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Property(self):
        return self.Property
    def set_Property(self, Property):
        self.Property = Property
    def add_Property(self, value):
        self.Property.append(value)
    def insert_Property_at(self, index, value):
        self.Property.insert(index, value)
    def replace_Property_at(self, index, value):
        self.Property[index] = value
    def _hasContent(self):
        if (
            self.Property
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='ClientInformationType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ClientInformationType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ClientInformationType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ClientInformationType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ClientInformationType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='common:', name_='ClientInformationType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='ClientInformationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Property_ in self.Property:
            namespaceprefix_ = self.Property_nsprefix_ + ':' if (UseCapturedNS_ and self.Property_nsprefix_) else ''
            Property_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Property', pretty_print=pretty_print)
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Property':
            obj_ = PropertyType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Property.append(obj_)
            obj_.original_tagname_ = 'Property'
# end class ClientInformationType


class RequestType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, RequestOption=None, SubVersion=None, TransactionReference=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if RequestOption is None:
            self.RequestOption = []
        else:
            self.RequestOption = RequestOption
        self.RequestOption_nsprefix_ = None
        self.SubVersion = SubVersion
        self.SubVersion_nsprefix_ = None
        self.TransactionReference = TransactionReference
        self.TransactionReference_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RequestType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RequestType.subclass:
            return RequestType.subclass(*args_, **kwargs_)
        else:
            return RequestType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_RequestOption(self):
        return self.RequestOption
    def set_RequestOption(self, RequestOption):
        self.RequestOption = RequestOption
    def add_RequestOption(self, value):
        self.RequestOption.append(value)
    def insert_RequestOption_at(self, index, value):
        self.RequestOption.insert(index, value)
    def replace_RequestOption_at(self, index, value):
        self.RequestOption[index] = value
    def get_SubVersion(self):
        return self.SubVersion
    def set_SubVersion(self, SubVersion):
        self.SubVersion = SubVersion
    def get_TransactionReference(self):
        return self.TransactionReference
    def set_TransactionReference(self, TransactionReference):
        self.TransactionReference = TransactionReference
    def _hasContent(self):
        if (
            self.RequestOption or
            self.SubVersion is not None or
            self.TransactionReference is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='RequestType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RequestType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RequestType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RequestType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RequestType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='common:', name_='RequestType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='RequestType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for RequestOption_ in self.RequestOption:
            namespaceprefix_ = self.RequestOption_nsprefix_ + ':' if (UseCapturedNS_ and self.RequestOption_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRequestOption>%s</%sRequestOption>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(RequestOption_), input_name='RequestOption')), namespaceprefix_ , eol_))
        if self.SubVersion is not None:
            namespaceprefix_ = self.SubVersion_nsprefix_ + ':' if (UseCapturedNS_ and self.SubVersion_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSubVersion>%s</%sSubVersion>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SubVersion), input_name='SubVersion')), namespaceprefix_ , eol_))
        if self.TransactionReference is not None:
            namespaceprefix_ = self.TransactionReference_nsprefix_ + ':' if (UseCapturedNS_ and self.TransactionReference_nsprefix_) else ''
            self.TransactionReference.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TransactionReference', pretty_print=pretty_print)
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'RequestOption':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'RequestOption')
            value_ = self.gds_validate_string(value_, node, 'RequestOption')
            self.RequestOption.append(value_)
            self.RequestOption_nsprefix_ = child_.prefix
        elif nodeName_ == 'SubVersion':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SubVersion')
            value_ = self.gds_validate_string(value_, node, 'SubVersion')
            self.SubVersion = value_
            self.SubVersion_nsprefix_ = child_.prefix
        elif nodeName_ == 'TransactionReference':
            obj_ = TransactionReferenceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TransactionReference = obj_
            obj_.original_tagname_ = 'TransactionReference'
# end class RequestType


class TransactionReferenceType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, CustomerContext=None, TransactionIdentifier=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.CustomerContext = CustomerContext
        self.CustomerContext_nsprefix_ = None
        self.TransactionIdentifier = TransactionIdentifier
        self.TransactionIdentifier_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TransactionReferenceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TransactionReferenceType.subclass:
            return TransactionReferenceType.subclass(*args_, **kwargs_)
        else:
            return TransactionReferenceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_CustomerContext(self):
        return self.CustomerContext
    def set_CustomerContext(self, CustomerContext):
        self.CustomerContext = CustomerContext
    def get_TransactionIdentifier(self):
        return self.TransactionIdentifier
    def set_TransactionIdentifier(self, TransactionIdentifier):
        self.TransactionIdentifier = TransactionIdentifier
    def _hasContent(self):
        if (
            self.CustomerContext is not None or
            self.TransactionIdentifier is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='TransactionReferenceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TransactionReferenceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TransactionReferenceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TransactionReferenceType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TransactionReferenceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='common:', name_='TransactionReferenceType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='TransactionReferenceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CustomerContext is not None:
            namespaceprefix_ = self.CustomerContext_nsprefix_ + ':' if (UseCapturedNS_ and self.CustomerContext_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCustomerContext>%s</%sCustomerContext>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CustomerContext), input_name='CustomerContext')), namespaceprefix_ , eol_))
        if self.TransactionIdentifier is not None:
            namespaceprefix_ = self.TransactionIdentifier_nsprefix_ + ':' if (UseCapturedNS_ and self.TransactionIdentifier_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTransactionIdentifier>%s</%sTransactionIdentifier>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TransactionIdentifier), input_name='TransactionIdentifier')), namespaceprefix_ , eol_))
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CustomerContext':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CustomerContext')
            value_ = self.gds_validate_string(value_, node, 'CustomerContext')
            self.CustomerContext = value_
            self.CustomerContext_nsprefix_ = child_.prefix
        elif nodeName_ == 'TransactionIdentifier':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TransactionIdentifier')
            value_ = self.gds_validate_string(value_, node, 'TransactionIdentifier')
            self.TransactionIdentifier = value_
            self.TransactionIdentifier_nsprefix_ = child_.prefix
# end class TransactionReferenceType


class ResponseType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ResponseStatus=None, Alert=None, AlertDetail=None, TransactionReference=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ResponseStatus = ResponseStatus
        self.ResponseStatus_nsprefix_ = "common"
        if Alert is None:
            self.Alert = []
        else:
            self.Alert = Alert
        self.Alert_nsprefix_ = "common"
        if AlertDetail is None:
            self.AlertDetail = []
        else:
            self.AlertDetail = AlertDetail
        self.AlertDetail_nsprefix_ = "common"
        self.TransactionReference = TransactionReference
        self.TransactionReference_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ResponseType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ResponseType.subclass:
            return ResponseType.subclass(*args_, **kwargs_)
        else:
            return ResponseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ResponseStatus(self):
        return self.ResponseStatus
    def set_ResponseStatus(self, ResponseStatus):
        self.ResponseStatus = ResponseStatus
    def get_Alert(self):
        return self.Alert
    def set_Alert(self, Alert):
        self.Alert = Alert
    def add_Alert(self, value):
        self.Alert.append(value)
    def insert_Alert_at(self, index, value):
        self.Alert.insert(index, value)
    def replace_Alert_at(self, index, value):
        self.Alert[index] = value
    def get_AlertDetail(self):
        return self.AlertDetail
    def set_AlertDetail(self, AlertDetail):
        self.AlertDetail = AlertDetail
    def add_AlertDetail(self, value):
        self.AlertDetail.append(value)
    def insert_AlertDetail_at(self, index, value):
        self.AlertDetail.insert(index, value)
    def replace_AlertDetail_at(self, index, value):
        self.AlertDetail[index] = value
    def get_TransactionReference(self):
        return self.TransactionReference
    def set_TransactionReference(self, TransactionReference):
        self.TransactionReference = TransactionReference
    def _hasContent(self):
        if (
            self.ResponseStatus is not None or
            self.Alert or
            self.AlertDetail or
            self.TransactionReference is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='ResponseType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ResponseType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ResponseType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ResponseType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ResponseType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='common:', name_='ResponseType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='ResponseType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ResponseStatus is not None:
            namespaceprefix_ = self.ResponseStatus_nsprefix_ + ':' if (UseCapturedNS_ and self.ResponseStatus_nsprefix_) else ''
            self.ResponseStatus.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ResponseStatus', pretty_print=pretty_print)
        for Alert_ in self.Alert:
            namespaceprefix_ = self.Alert_nsprefix_ + ':' if (UseCapturedNS_ and self.Alert_nsprefix_) else ''
            Alert_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Alert', pretty_print=pretty_print)
        for AlertDetail_ in self.AlertDetail:
            namespaceprefix_ = self.AlertDetail_nsprefix_ + ':' if (UseCapturedNS_ and self.AlertDetail_nsprefix_) else ''
            AlertDetail_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='AlertDetail', pretty_print=pretty_print)
        if self.TransactionReference is not None:
            namespaceprefix_ = self.TransactionReference_nsprefix_ + ':' if (UseCapturedNS_ and self.TransactionReference_nsprefix_) else ''
            self.TransactionReference.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TransactionReference', pretty_print=pretty_print)
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ResponseStatus':
            obj_ = CodeDescriptionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ResponseStatus = obj_
            obj_.original_tagname_ = 'ResponseStatus'
        elif nodeName_ == 'Alert':
            obj_ = CodeDescriptionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Alert.append(obj_)
            obj_.original_tagname_ = 'Alert'
        elif nodeName_ == 'AlertDetail':
            obj_ = DetailType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.AlertDetail.append(obj_)
            obj_.original_tagname_ = 'AlertDetail'
        elif nodeName_ == 'TransactionReference':
            obj_ = TransactionReferenceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TransactionReference = obj_
            obj_.original_tagname_ = 'TransactionReference'
# end class ResponseType


class CodeDescriptionType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Code=None, Description=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Code = Code
        self.Code_nsprefix_ = None
        self.Description = Description
        self.Description_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CodeDescriptionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CodeDescriptionType.subclass:
            return CodeDescriptionType.subclass(*args_, **kwargs_)
        else:
            return CodeDescriptionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Code(self):
        return self.Code
    def set_Code(self, Code):
        self.Code = Code
    def get_Description(self):
        return self.Description
    def set_Description(self, Description):
        self.Description = Description
    def _hasContent(self):
        if (
            self.Code is not None or
            self.Description is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='CodeDescriptionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CodeDescriptionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CodeDescriptionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CodeDescriptionType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CodeDescriptionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='common:', name_='CodeDescriptionType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='CodeDescriptionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Code is not None:
            namespaceprefix_ = self.Code_nsprefix_ + ':' if (UseCapturedNS_ and self.Code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCode>%s</%sCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Code), input_name='Code')), namespaceprefix_ , eol_))
        if self.Description is not None:
            namespaceprefix_ = self.Description_nsprefix_ + ':' if (UseCapturedNS_ and self.Description_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDescription>%s</%sDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Description), input_name='Description')), namespaceprefix_ , eol_))
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Code')
            value_ = self.gds_validate_string(value_, node, 'Code')
            self.Code = value_
            self.Code_nsprefix_ = child_.prefix
        elif nodeName_ == 'Description':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Description')
            value_ = self.gds_validate_string(value_, node, 'Description')
            self.Description = value_
            self.Description_nsprefix_ = child_.prefix
# end class CodeDescriptionType


class DetailType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Code=None, Description=None, ElementLevelInformation=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Code = Code
        self.Code_nsprefix_ = None
        self.Description = Description
        self.Description_nsprefix_ = None
        self.ElementLevelInformation = ElementLevelInformation
        self.ElementLevelInformation_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DetailType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DetailType.subclass:
            return DetailType.subclass(*args_, **kwargs_)
        else:
            return DetailType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Code(self):
        return self.Code
    def set_Code(self, Code):
        self.Code = Code
    def get_Description(self):
        return self.Description
    def set_Description(self, Description):
        self.Description = Description
    def get_ElementLevelInformation(self):
        return self.ElementLevelInformation
    def set_ElementLevelInformation(self, ElementLevelInformation):
        self.ElementLevelInformation = ElementLevelInformation
    def _hasContent(self):
        if (
            self.Code is not None or
            self.Description is not None or
            self.ElementLevelInformation is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='DetailType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DetailType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DetailType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DetailType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DetailType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='common:', name_='DetailType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='DetailType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Code is not None:
            namespaceprefix_ = self.Code_nsprefix_ + ':' if (UseCapturedNS_ and self.Code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCode>%s</%sCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Code), input_name='Code')), namespaceprefix_ , eol_))
        if self.Description is not None:
            namespaceprefix_ = self.Description_nsprefix_ + ':' if (UseCapturedNS_ and self.Description_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDescription>%s</%sDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Description), input_name='Description')), namespaceprefix_ , eol_))
        if self.ElementLevelInformation is not None:
            namespaceprefix_ = self.ElementLevelInformation_nsprefix_ + ':' if (UseCapturedNS_ and self.ElementLevelInformation_nsprefix_) else ''
            self.ElementLevelInformation.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ElementLevelInformation', pretty_print=pretty_print)
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Code')
            value_ = self.gds_validate_string(value_, node, 'Code')
            self.Code = value_
            self.Code_nsprefix_ = child_.prefix
        elif nodeName_ == 'Description':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Description')
            value_ = self.gds_validate_string(value_, node, 'Description')
            self.Description = value_
            self.Description_nsprefix_ = child_.prefix
        elif nodeName_ == 'ElementLevelInformation':
            obj_ = ElementLevelInformationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ElementLevelInformation = obj_
            obj_.original_tagname_ = 'ElementLevelInformation'
# end class DetailType


class ElementLevelInformationType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Level=None, ElementIdentifier=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Level = Level
        self.Level_nsprefix_ = None
        if ElementIdentifier is None:
            self.ElementIdentifier = []
        else:
            self.ElementIdentifier = ElementIdentifier
        self.ElementIdentifier_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ElementLevelInformationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ElementLevelInformationType.subclass:
            return ElementLevelInformationType.subclass(*args_, **kwargs_)
        else:
            return ElementLevelInformationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Level(self):
        return self.Level
    def set_Level(self, Level):
        self.Level = Level
    def get_ElementIdentifier(self):
        return self.ElementIdentifier
    def set_ElementIdentifier(self, ElementIdentifier):
        self.ElementIdentifier = ElementIdentifier
    def add_ElementIdentifier(self, value):
        self.ElementIdentifier.append(value)
    def insert_ElementIdentifier_at(self, index, value):
        self.ElementIdentifier.insert(index, value)
    def replace_ElementIdentifier_at(self, index, value):
        self.ElementIdentifier[index] = value
    def _hasContent(self):
        if (
            self.Level is not None or
            self.ElementIdentifier
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='ElementLevelInformationType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ElementLevelInformationType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ElementLevelInformationType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ElementLevelInformationType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ElementLevelInformationType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='common:', name_='ElementLevelInformationType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='ElementLevelInformationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Level is not None:
            namespaceprefix_ = self.Level_nsprefix_ + ':' if (UseCapturedNS_ and self.Level_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sLevel>%s</%sLevel>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Level), input_name='Level')), namespaceprefix_ , eol_))
        for ElementIdentifier_ in self.ElementIdentifier:
            namespaceprefix_ = self.ElementIdentifier_nsprefix_ + ':' if (UseCapturedNS_ and self.ElementIdentifier_nsprefix_) else ''
            ElementIdentifier_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ElementIdentifier', pretty_print=pretty_print)
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Level':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Level')
            value_ = self.gds_validate_string(value_, node, 'Level')
            self.Level = value_
            self.Level_nsprefix_ = child_.prefix
        elif nodeName_ == 'ElementIdentifier':
            obj_ = ElementIdentifierType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ElementIdentifier.append(obj_)
            obj_.original_tagname_ = 'ElementIdentifier'
# end class ElementLevelInformationType


class ElementIdentifierType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Code=None, Value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Code = Code
        self.Code_nsprefix_ = None
        self.Value = Value
        self.Value_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ElementIdentifierType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ElementIdentifierType.subclass:
            return ElementIdentifierType.subclass(*args_, **kwargs_)
        else:
            return ElementIdentifierType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Code(self):
        return self.Code
    def set_Code(self, Code):
        self.Code = Code
    def get_Value(self):
        return self.Value
    def set_Value(self, Value):
        self.Value = Value
    def _hasContent(self):
        if (
            self.Code is not None or
            self.Value is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='ElementIdentifierType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ElementIdentifierType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ElementIdentifierType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ElementIdentifierType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ElementIdentifierType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='common:', name_='ElementIdentifierType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='ElementIdentifierType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Code is not None:
            namespaceprefix_ = self.Code_nsprefix_ + ':' if (UseCapturedNS_ and self.Code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCode>%s</%sCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Code), input_name='Code')), namespaceprefix_ , eol_))
        if self.Value is not None:
            namespaceprefix_ = self.Value_nsprefix_ + ':' if (UseCapturedNS_ and self.Value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValue>%s</%sValue>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Value), input_name='Value')), namespaceprefix_ , eol_))
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Code')
            value_ = self.gds_validate_string(value_, node, 'Code')
            self.Code = value_
            self.Code_nsprefix_ = child_.prefix
        elif nodeName_ == 'Value':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Value')
            value_ = self.gds_validate_string(value_, node, 'Value')
            self.Value = value_
            self.Value_nsprefix_ = child_.prefix
# end class ElementIdentifierType


class PropertyType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Key=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Key = _cast(None, Key)
        self.Key_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PropertyType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PropertyType.subclass:
            return PropertyType.subclass(*args_, **kwargs_)
        else:
            return PropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Key(self):
        return self.Key
    def set_Key(self, Key):
        self.Key = Key
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PropertyType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PropertyType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PropertyType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PropertyType')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PropertyType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PropertyType'):
        if self.Key is not None and 'Key' not in already_processed:
            already_processed.add('Key')
            outfile.write(' Key=%s' % (quote_attrib(self.Key), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PropertyType', fromsubclass_=False, pretty_print=True):
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
        value = find_attr_value_('Key', node)
        if value is not None and 'Key' not in already_processed:
            already_processed.add('Key')
            self.Key = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class PropertyType


GDSClassesMapping = {
    'ClientInformation': ClientInformationType,
    'Request': RequestType,
    'Response': ResponseType,
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
        rootTag = 'ResponseShipListAddressType'
        rootClass = ResponseShipListAddressType
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
               mapping=None, reverse_mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ResponseShipListAddressType'
        rootClass = ResponseShipListAddressType
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if mapping is None:
        mapping = {}
    if reverse_mapping is None:
        reverse_mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping,
        reverse_mapping_=reverse_mapping, nsmap_=nsmap)
    reverse_node_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
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
    return rootObj, rootElement, mapping, reverse_node_mapping


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
        rootTag = 'ResponseShipListAddressType'
        rootClass = ResponseShipListAddressType
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:tnt="http://www.ups.com/XMLSchema/XOLTWS/tnt/v1.0"')
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
        rootTag = 'ResponseShipListAddressType'
        rootClass = ResponseShipListAddressType
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from time_in_transit_web_service_schema import *\n\n')
        sys.stdout.write('import time_in_transit_web_service_schema as model_\n\n')
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
    "{http://www.ups.com/XMLSchema/XOLTWS/tnt/v1.0}CodeDescriptionType": "CodeDescriptionType1",
}

#
# Mapping of namespaces to types defined in them
# and the file in which each is defined.
# simpleTypes are marked "ST" and complexTypes "CT".
NamespaceToDefMappings_ = {'http://www.ups.com/XMLSchema/XOLTWS/Common/v1.0': [('ClientInformationType',
                                                      './schemas/common.xsd',
                                                      'CT'),
                                                     ('RequestType',
                                                      './schemas/common.xsd',
                                                      'CT'),
                                                     ('TransactionReferenceType',
                                                      './schemas/common.xsd',
                                                      'CT'),
                                                     ('ResponseType',
                                                      './schemas/common.xsd',
                                                      'CT'),
                                                     ('CodeDescriptionType',
                                                      './schemas/common.xsd',
                                                      'CT'),
                                                     ('DetailType',
                                                      './schemas/common.xsd',
                                                      'CT'),
                                                     ('ElementLevelInformationType',
                                                      './schemas/common.xsd',
                                                      'CT'),
                                                     ('ElementIdentifierType',
                                                      './schemas/common.xsd',
                                                      'CT')],
 'http://www.ups.com/XMLSchema/XOLTWS/tnt/v1.0': [('ResponseShipListAddressType',
                                                   './schemas/TimeInTransitWebServiceSchema.xsd',
                                                   'CT'),
                                                  ('RequestShipFromAddressType',
                                                   './schemas/TimeInTransitWebServiceSchema.xsd',
                                                   'CT'),
                                                  ('RequestShipToAddressType',
                                                   './schemas/TimeInTransitWebServiceSchema.xsd',
                                                   'CT'),
                                                  ('ResponseShipFromAddressType',
                                                   './schemas/TimeInTransitWebServiceSchema.xsd',
                                                   'CT'),
                                                  ('ResponseShipToAddressType',
                                                   './schemas/TimeInTransitWebServiceSchema.xsd',
                                                   'CT'),
                                                  ('RequestShipFromType',
                                                   './schemas/TimeInTransitWebServiceSchema.xsd',
                                                   'CT'),
                                                  ('RequestShipToType',
                                                   './schemas/TimeInTransitWebServiceSchema.xsd',
                                                   'CT'),
                                                  ('ResponseShipFromType',
                                                   './schemas/TimeInTransitWebServiceSchema.xsd',
                                                   'CT'),
                                                  ('ResponseShipToType',
                                                   './schemas/TimeInTransitWebServiceSchema.xsd',
                                                   'CT'),
                                                  ('ShipmentWeightType',
                                                   './schemas/TimeInTransitWebServiceSchema.xsd',
                                                   'CT'),
                                                  ('CodeDescriptionType',
                                                   './schemas/TimeInTransitWebServiceSchema.xsd',
                                                   'CT'),
                                                  ('PickupType',
                                                   './schemas/TimeInTransitWebServiceSchema.xsd',
                                                   'CT'),
                                                  ('InvoiceLineTotalType',
                                                   './schemas/TimeInTransitWebServiceSchema.xsd',
                                                   'CT'),
                                                  ('ReturnContractServicesType',
                                                   './schemas/TimeInTransitWebServiceSchema.xsd',
                                                   'CT'),
                                                  ('EstimatedArrivalType',
                                                   './schemas/TimeInTransitWebServiceSchema.xsd',
                                                   'CT'),
                                                  ('ServiceSummaryType',
                                                   './schemas/TimeInTransitWebServiceSchema.xsd',
                                                   'CT'),
                                                  ('TransitResponseType',
                                                   './schemas/TimeInTransitWebServiceSchema.xsd',
                                                   'CT'),
                                                  ('CandidateType',
                                                   './schemas/TimeInTransitWebServiceSchema.xsd',
                                                   'CT'),
                                                  ('ShipListType',
                                                   './schemas/TimeInTransitWebServiceSchema.xsd',
                                                   'CT'),
                                                  ('CandidateResponseType',
                                                   './schemas/TimeInTransitWebServiceSchema.xsd',
                                                   'CT')]}

__all__ = [
    "CandidateResponseType",
    "CandidateType",
    "ClientInformationType",
    "CodeDescriptionType",
    "CodeDescriptionType1",
    "DetailType",
    "ElementIdentifierType",
    "ElementLevelInformationType",
    "EstimatedArrivalType",
    "InvoiceLineTotalType",
    "PickupType",
    "PropertyType",
    "RequestShipFromAddressType",
    "RequestShipFromType",
    "RequestShipToAddressType",
    "RequestShipToType",
    "RequestType",
    "ResponseShipFromAddressType",
    "ResponseShipFromType",
    "ResponseShipListAddressType",
    "ResponseShipToAddressType",
    "ResponseShipToType",
    "ResponseType",
    "ReturnContractServicesType",
    "ServiceSummaryType",
    "ShipListType",
    "ShipmentWeightType",
    "TimeInTransitRequest",
    "TimeInTransitResponse",
    "TransactionReferenceType",
    "TransitResponseType"
]
