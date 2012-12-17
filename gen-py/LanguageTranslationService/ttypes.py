#
# Autogenerated by Thrift Compiler (1.0.0-dev)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:utf8strings
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class PartOfSpeech:
  Adjective = 1
  Adverb = 2
  Noun = 3
  Verb = 4

  ValueToNames = {
    1: "Adjective",
    2: "Adverb",
    3: "Noun",
    4: "Verb",
  }

  NameToValues = {
    "Adjective": 1,
    "Adverb": 2,
    "Noun": 3,
    "Verb": 4,
  }


class TranslateOneDictionary:
  """
  Attributes:
   - nameDictionary
   - translate
   - sameTypeSequence
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'nameDictionary', None, None, ), # 1
    (2, TType.STRING, 'translate', None, None, ), # 2
    (3, TType.STRING, 'sameTypeSequence', None, None, ), # 3
  )

  def __init__(self, nameDictionary=None, translate=None, sameTypeSequence=None,):
    self.nameDictionary = nameDictionary
    self.translate = translate
    self.sameTypeSequence = sameTypeSequence

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.nameDictionary = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.translate = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.sameTypeSequence = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TranslateOneDictionary')
    if self.nameDictionary is not None:
      oprot.writeFieldBegin('nameDictionary', TType.STRING, 1)
      oprot.writeString(self.nameDictionary.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.translate is not None:
      oprot.writeFieldBegin('translate', TType.STRING, 2)
      oprot.writeString(self.translate.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.sameTypeSequence is not None:
      oprot.writeFieldBegin('sameTypeSequence', TType.STRING, 3)
      oprot.writeString(self.sameTypeSequence.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TranslatePackage:
  """
  Attributes:
   - word
   - lemma
   - partOfSpeech
   - translations
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'word', None, None, ), # 1
    (2, TType.STRING, 'lemma', None, None, ), # 2
    (3, TType.I32, 'partOfSpeech', None, None, ), # 3
    (4, TType.LIST, 'translations', (TType.STRUCT,(TranslateOneDictionary, TranslateOneDictionary.thrift_spec)), None, ), # 4
  )

  def __init__(self, word=None, lemma=None, partOfSpeech=None, translations=None,):
    self.word = word
    self.lemma = lemma
    self.partOfSpeech = partOfSpeech
    self.translations = translations

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.word = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.lemma = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.partOfSpeech = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.translations = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = TranslateOneDictionary()
            _elem5.read(iprot)
            self.translations.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TranslatePackage')
    if self.word is not None:
      oprot.writeFieldBegin('word', TType.STRING, 1)
      oprot.writeString(self.word.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.lemma is not None:
      oprot.writeFieldBegin('lemma', TType.STRING, 2)
      oprot.writeString(self.lemma.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.partOfSpeech is not None:
      oprot.writeFieldBegin('partOfSpeech', TType.I32, 3)
      oprot.writeI32(self.partOfSpeech)
      oprot.writeFieldEnd()
    if self.translations is not None:
      oprot.writeFieldBegin('translations', TType.LIST, 4)
      oprot.writeListBegin(TType.STRUCT, len(self.translations))
      for iter6 in self.translations:
        iter6.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class InvalidValueException(TException):
  """
  Attributes:
   - errorCode
   - errorMsg
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'errorCode', None, None, ), # 1
    (2, TType.STRING, 'errorMsg', None, None, ), # 2
  )

  def __init__(self, errorCode=None, errorMsg=None,):
    self.errorCode = errorCode
    self.errorMsg = errorMsg

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.errorCode = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.errorMsg = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('InvalidValueException')
    if self.errorCode is not None:
      oprot.writeFieldBegin('errorCode', TType.I32, 1)
      oprot.writeI32(self.errorCode)
      oprot.writeFieldEnd()
    if self.errorMsg is not None:
      oprot.writeFieldBegin('errorMsg', TType.STRING, 2)
      oprot.writeString(self.errorMsg.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __str__(self):
    return repr(self)

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)