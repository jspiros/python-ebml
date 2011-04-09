from .base import *


class SegmentElement(Element):
	class_id = 0x18538067
	class_name = 'Segment'
	class_root = True
	data_type = CONTAINER


class SeekHeadElement(Element):
	class_id = 0x114d9b74
	class_name = 'SeekHead'
	class_parents = (SegmentElement,)
	data_type = CONTAINER


class SeekElement(Element):
	class_id = 0x4dbb
	class_name = 'Seek'
	class_parents = (SeekHeadElement,)
	data_type = CONTAINER


class SeekIDElement(Element):
	class_id = 0x53ab
	class_name = 'SeekID'
	class_parents = (SeekElement,)
	data_type = BINARY


class SeekPositionElement(Element):
	class_id = 0x53ac
	class_name = 'SeekPosition'
	class_parents = (SeekElement,)
	data_type = UINT


class InfoElement(Element):
	class_id = 0x1549a966
	class_name = 'Info'
	class_parents = (SegmentElement,)
	data_type = CONTAINER


class SegmentUIDElement(Element):
	class_id = 0x73a4
	class_name = 'SegmentUID'
	class_parents = (InfoElement,)
	data_type = BINARY


class SegmentFilenameElement(Element):
	class_id = 0x7384
	class_name = 'SegmentFilename'
	class_parents = (InfoElement,)
	data_type = UNICODE


class PrevUIDElement(Element):
	class_id = 0x3cb923
	class_name = 'PrevUID'
	class_parents = (InfoElement,)
	data_type = BINARY


class PrevFilenameElement(Element):
	class_id = 0x3c83ab
	class_name = 'PrevFilename'
	class_parents = (InfoElement,)
	data_type = UNICODE


class NextUIDElement(Element):
	class_id = 0x3eb923
	class_name = 'NextUID'
	class_parents = (InfoElement,)
	data_type = BINARY


class NextFilenameElement(Element):
	class_id = 0x3e83bb
	class_name = 'NextFilename'
	class_parents = (InfoElement,)
	data_type = UNICODE


class SegmentFamilyElement(Element):
	class_id = 0x4444
	class_name = 'SegmentFamily'
	class_parents = (InfoElement,)
	data_type = BINARY


class ChapterTranslateElement(Element):
	class_id = 0x6924
	class_name = 'ChapterTranslate'
	class_parents = (InfoElement,)
	data_type = CONTAINER


class ChapterTranslateEditionUIDElement(Element):
	class_id = 0x69FC
	class_name = 'ChapterTranslateEditionUID'
	class_parents = (ChapterTranslateElement,)
	data_type = UINT


class ChapterTranslateCodecElement(Element):
	class_id = 0x69bf
	class_name = 'ChapterTranslateCodec'
	class_parents = (ChapterTranslateElement,)
	data_type = UINT


class ChapterTranslateIDElement(Element):
	class_id = 0x69a5
	class_name = 'ChapterTranslateID'
	class_parents = (ChapterTranslateElement,)
	data_type = BINARY


class TimecodeScaleElement(Element):
	class_id = 0x2ad7b1
	class_name = 'TimecodeScale'
	class_parents = (InfoElement,)
	data_type = UINT


class DurationElement(Element):
	class_id = 0x4489
	class_name = 'Duration'
	class_parents = (InfoElement,)
	data_type = FLOAT


class DateUTCElement(Element):
	class_id = 0x4461
	class_name = 'DateUTC'
	class_parents = (InfoElement,)
	data_type = DATE


class TitleElement(Element):
	class_id = 0x7ba9
	class_name = 'Title'
	class_parents = (InfoElement,)
	data_type = UNICODE


class MuxingAppElement(Element):
	class_id = 0x4d80
	class_name = 'MuxingApp'
	class_parents = (InfoElement,)
	data_type = UNICODE


class WritingAppElement(Element):
	class_id = 0x5741
	class_name = 'WritingApp'
	class_parents = (InfoElement,)
	data_type = UNICODE


class ClusterElement(Element):
	class_id = 0x1f43b675
	class_name = 'Cluster'
	class_parents = (SegmentElement,)
	data_type = CONTAINER


class TimecodeElement(Element):
	class_id = 0xe7
	class_name = 'Timecode'
	class_parents = (ClusterElement,)
	data_type = UINT


class SilentTracksElement(Element):
	class_id = 0x5854
	class_name = 'SilentTracks'
	class_parents = (ClusterElement,)
	data_type = CONTAINER


class SilentTrackNumberElement(Element):
	class_id = 0x58d7
	class_name = 'SilentTrackNumber'
	class_parents = (SilentTracksElement,)
	data_type = UINT


class PositionElement(Element):
	class_id = 0xa7
	class_name = 'Position'
	class_parents = (ClusterElement,)
	data_type = UINT


class PrevSizeElement(Element):
	class_id = 0xab
	class_name = 'PrevSize'
	class_parents = (ClusterElement,)
	data_type = UINT


class SimpleBlockElement(Element):
	class_id = 0xa3
	class_name = 'SimpleBlock'
	class_parents = (ClusterElement,)
	data_type = BINARY


class BlockGroupElement(Element):
	class_id = 0xa0
	class_name = 'BlockGroup'
	class_parents = (ClusterElement,)
	data_type = CONTAINER


class BlockElement(Element):
	class_id = 0xa1
	class_name = 'Block'
	class_parents = (BlockGroupElement,)
	data_type = BINARY


class BlockVirtualElement(Element):
	class_id = 0xa2
	class_name = 'BlockVirtual'
	class_parents = (BlockGroupElement,)
	data_type = BINARY


class BlockAdditionsElement(Element):
	class_id = 0x75a1
	class_name = 'BlockAdditions'
	class_parents = (BlockGroupElement,)
	data_type = CONTAINER


class BlockMoreElement(Element):
	class_id = 0xa6
	class_name = 'BlockMore'
	class_parents = (BlockAdditionsElement,)
	data_type = CONTAINER


class BlockAddIDElement(Element):
	class_id = 0xee
	class_name = 'BlockAddID'
	class_parents = (BlockMoreElement,)
	data_type = UINT


class BlockAdditionalElement(Element):
	class_id = 0xa5
	class_name = 'BlockAdditional'
	class_parents = (BlockMoreElement,)
	data_type = BINARY


class BlockDurationElement(Element):
	class_id = 0x9b
	class_name = 'BlockDuration'
	class_parents = (BlockGroupElement,)
	data_type = UINT


class ReferencePriorityElement(Element):
	class_id = 0xfa
	class_name = 'ReferencePriority'
	class_parents = (BlockGroupElement,)
	data_type = UINT


class ReferenceBlockElement(Element):
	class_id = 0xfb
	class_name = 'ReferenceBlock'
	class_parents = (BlockGroupElement,)
	data_type = INT


class ReferenceVirtualElement(Element):
	class_id = 0xfd
	class_name = 'ReferenceVirtual'
	class_parents = (BlockGroupElement,)
	data_type = INT


class CodecStateElement(Element):
	class_id = 0xa4
	class_name = 'CodecState'
	class_parents = (BlockGroupElement,)
	data_type = BINARY


class SlicesElement(Element):
	class_id = 0x8e
	class_name = 'Slices'
	class_parents = (BlockGroupElement,)
	data_type = CONTAINER


class TimeSliceElement(Element):
	class_id = 0xe8
	class_name = 'TimeSlice'
	class_parents = (SlicesElement,)
	data_type = CONTAINER


class LaceNumberElement(Element):
	class_id = 0xcc
	class_name = 'LaceNumber'
	class_parents = (TimeSliceElement,)
	data_type = UINT


class FrameNumberElement(Element):
	class_id = 0xcd
	class_name = 'FrameNumber'
	class_parents = (TimeSliceElement,)
	data_type = UINT


class BlockAdditionIDElement(Element):
	class_id = 0xcb
	class_name = 'BlockAdditionID'
	class_parents = (TimeSliceElement,)
	data_type = UINT


class DelayElement(Element):
	class_id = 0xce
	class_name = 'Delay'
	class_parents = (TimeSliceElement,)
	data_type = UINT


class SliceDurationElement(Element):
	class_id = 0xcf
	class_name = 'SliceDuration'
	class_parents = (TimeSliceElement,)
	data_type = UINT


class ReferenceFrameElement(Element):
	class_id = 0xc8
	class_name = 'ReferenceFrame'
	class_parents = (BlockGroupElement,)
	data_type = CONTAINER


class ReferenceOffsetElement(Element):
	class_id = 0xc9
	class_name = 'ReferenceOffset'
	class_parents = (ReferenceFrameElement,)
	data_type = UINT


class ReferenceTimeCodeElement(Element):
	class_id = 0xca
	class_name = 'ReferenceTimeCode'
	class_parents = (ReferenceFrameElement,)
	data_type = UINT


class EncryptedBlockElement(Element):
	class_id = 0xaf
	class_name = 'EncryptedBlock'
	class_parents = (ClusterElement,)
	data_type = BINARY


class TracksElement(Element):
	class_id = 0x1654ae6b
	class_name = 'Tracks'
	class_parents = (SegmentElement,)
	data_type = CONTAINER


class TrackEntryElement(Element):
	class_id = 0xae
	class_name = 'TrackEntry'
	class_parents = (TracksElement,)
	data_type = CONTAINER


class TrackNumberElement(Element):
	class_id = 0xd7
	class_name = 'TrackNumber'
	class_parents = (TrackEntryElement,)
	data_type = UINT


class TrackUIDElement(Element):
	class_id = 0x73c5
	class_name = 'TrackUID'
	class_parents = (TrackEntryElement,)
	data_type = UINT


class TrackTypeElement(Element):
	class_id = 0x83
	class_name = 'TrackType'
	class_parents = (TrackEntryElement,)
	data_type = UINT


class FlagEnabledElement(Element):
	class_id = 0xb9
	class_name = 'FlagEnabled'
	class_parents = (TrackEntryElement,)
	data_type = UINT


class FlagDefaultElement(Element):
	class_id = 0x88
	class_name = 'FlagDefault'
	class_parents = (TrackEntryElement,)
	data_type = UINT


class FlagForcedElement(Element):
	class_id = 0x55aa
	class_name = 'FlagForced'
	class_parents = (TrackEntryElement,)
	data_type = UINT


class FlagLacingElement(Element):
	class_id = 0x9c
	class_name = 'FlagLacing'
	class_parents = (TrackEntryElement,)
	data_type = UINT


class MinCacheElement(Element):
	class_id = 0x6de7
	class_name = 'MinCache'
	class_parents = (TrackEntryElement,)
	data_type = UINT


class MaxCacheElement(Element):
	class_id = 0x6df8
	class_name = 'MaxCache'
	class_parents = (TrackEntryElement,)
	data_type = UINT


class DefaultDurationElement(Element):
	class_id = 0x23e383
	class_name = 'DefaultDuration'
	class_parents = (TrackEntryElement,)
	data_type = UINT


class TrackTimecodeScaleElement(Element):
	class_id = 0x23314f
	class_name = 'TrackTimecodeScale'
	class_parents = (TrackEntryElement,)
	data_type = FLOAT


class TrackOffsetElement(Element):
	class_id = 0x537F
	class_name = 'TrackOffset'
	class_parents = (TrackEntryElement,)
	data_type = INT


class MaxBlockAdditionIDElement(Element):
	class_id = 0x55EE
	class_name = 'MaxBlockAdditionID'
	class_parents = (TrackEntryElement,)
	data_type = UINT


class NameElement(Element):
	class_id = 0x536E
	class_name = 'Name'
	class_parents = (TrackEntryElement,)
	data_type = UNICODE


class LanguageElement(Element):
	class_id = 0x22B59C
	class_name = 'Language'
	class_parents = (TrackEntryElement,)
	data_type = STRING


class CodecIDElement(Element):
	class_id = 0x86
	class_name = 'CodecID'
	class_parents = (TrackEntryElement,)
	data_type = STRING


class CodecPrivateElement(Element):
	class_id = 0x63A2
	class_name = 'CodecPrivate'
	class_parents = (TrackEntryElement,)
	data_type = BINARY


class CodecNameElement(Element):
	class_id = 0x258688
	class_name = 'CodecName'
	class_parents = (TrackEntryElement,)
	data_type = UNICODE


class AttachmentLinkElement(Element):
	class_id = 0x7446
	class_name = 'AttachmentLink'
	class_parents = (TrackEntryElement,)
	data_type = UINT


class CodecSettingsElement(Element):
	class_id = 0x3A9697
	class_name = 'CodecSettings'
	class_parents = (TrackEntryElement,)
	data_type = UNICODE


class CodecInfoURLElement(Element):
	class_id = 0x3B4040
	class_name = 'CodecInfoURL'
	class_parents = (TrackEntryElement,)
	data_type = STRING


class CodecDownloadURLElement(Element):
	class_id = 0x26B240
	class_name = 'CodecDownloadURL'
	class_parents = (TrackEntryElement,)
	data_type = STRING


class CodecDecodeAllElement(Element):
	class_id = 0xAA
	class_name = 'CodecDecodeAll'
	class_parents = (TrackEntryElement,)
	data_type = UINT


class TrackOverlayElement(Element):
	class_id = 0x6FAB
	class_name = 'TrackOverlay'
	class_parents = (TrackEntryElement,)
	data_type = UINT


class TrackTranslateElement(Element):
	class_id = 0x6624
	class_name = 'TrackTranslate'
	class_parents = (TrackEntryElement,)
	data_type = CONTAINER


class TrackTranslateEditionUIDElement(Element):
	class_id = 0x66FC
	class_name = 'TrackTranslateEditionUID'
	class_parents = (TrackTranslateElement,)
	data_type = UINT


class TrackTranslateCodecElement(Element):
	class_id = 0x66BF
	class_name = 'TrackTranslateCodec'
	class_parents = (TrackTranslateElement,)
	data_type = UINT


class TrackTranslateTrackIDElement(Element):
	class_id = 0x66A5
	class_name = 'TrackTranslateTrackID'
	class_parents = (TrackTranslateElement,)
	data_type = BINARY


class VideoElement(Element):
	class_id = 0xE0
	class_name = 'Video'
	class_parents = (TrackEntryElement,)
	data_type = CONTAINER


class FlagInterlacedElement(Element):
	class_id = 0x9A
	class_name = 'FlagInterlaced'
	class_parents = (VideoElement,)
	data_type = UINT


class StereoModeElement(Element):
	class_id = 0x53B8
	class_name = 'StereoMode'
	class_parents = (VideoElement,)
	data_type = UINT


class OldStereoModeElement(Element):
	class_id = 0x53B9
	class_name = 'OldStereoMode'
	class_parents = (VideoElement,)
	data_type = UINT


class PixelWidthElement(Element):
	class_id = 0xB0
	class_name = 'PixelWidth'
	class_parents = (VideoElement,)
	data_type = UINT


class PixelHeightElement(Element):
	class_id = 0xBA
	class_name = 'PixelHeight'
	class_parents = (VideoElement,)
	data_type = UINT


class PixelCropBottomElement(Element):
	class_id = 0x54AA
	class_name = 'PixelCropBottom'
	class_parents = (VideoElement,)
	data_type = UINT


class PixelCropTopElement(Element):
	class_id = 0x54BB
	class_name = 'PixelCropTop'
	class_parents = (VideoElement,)
	data_type = UINT


class PixelCropLeftElement(Element):
	class_id = 0x54CC
	class_name = 'PixelCropLeft'
	class_parents = (VideoElement,)
	data_type = UINT


class PixelCropRightElement(Element):
	class_id = 0x54DD
	class_name = 'PixelCropRight'
	class_parents = (VideoElement,)
	data_type = UINT


class DisplayWidthElement(Element):
	class_id = 0x54B0
	class_name = 'DisplayWidth'
	class_parents = (VideoElement,)
	data_type = UINT


class DisplayHeightElement(Element):
	class_id = 0x54BA
	class_name = 'DisplayHeight'
	class_parents = (VideoElement,)
	data_type = UINT


class DisplayUnitElement(Element):
	class_id = 0x54B2
	class_name = 'DisplayUnit'
	class_parents = (VideoElement,)
	data_type = UINT


class AspectRatioTypeElement(Element):
	class_id = 0x54B3
	class_name = 'AspectRatioType'
	class_parents = (VideoElement,)
	data_type = UINT


class ColourSpaceElement(Element):
	class_id = 0x2EB524
	class_name = 'ColourSpace'
	class_parents = (VideoElement,)
	data_type = BINARY


class GammaValueElement(Element):
	class_id = 0x2FB523
	class_name = 'GammaValue'
	class_parents = (VideoElement,)
	data_type = FLOAT


class FrameRateElement(Element):
	class_id = 0x2383E3
	class_name = 'FrameRate'
	class_parents = (VideoElement,)
	data_type = FLOAT


class AudioElement(Element):
	class_id = 0xE1
	class_name = 'Audio'
	class_parents = (TrackEntryElement,)
	data_type = CONTAINER


class SamplingFrequencyElement(Element):
	class_id = 0xB5
	class_name = 'SamplingFrequency'
	class_parents = (AudioElement,)
	data_type = FLOAT


class OutputSamplingFrequencyElement(Element):
	class_id = 0x78B5
	class_name = 'OutputSamplingFrequency'
	class_parents = (AudioElement,)
	data_type = FLOAT


class ChannelsElement(Element):
	class_id = 0x9F
	class_name = 'Channels'
	class_parents = (AudioElement,)
	data_type = UINT


class ChannelPositionsElement(Element):
	class_id = 0x7D7B
	class_name = 'ChannelPositions'
	class_parents = (AudioElement,)
	data_type = BINARY


class BitDepthElement(Element):
	class_id = 0x6264
	class_name = 'BitDepth'
	class_parents = (AudioElement,)
	data_type = UINT


class TrackOperationElement(Element):
	class_id = 0xE2
	class_name = 'TrackOperation'
	class_parents = (TrackEntryElement,)
	data_type = CONTAINER


class TrackCombinePlanesElement(Element):
	class_id = 0xE3
	class_name = 'TrackCombinePlanes'
	class_parents = (TrackOperationElement,)
	data_type = CONTAINER


class TrackPlaneElement(Element):
	class_id = 0xE4
	class_name = 'TrackPlane'
	class_parents = (TrackCombinePlanesElement,)
	data_type = CONTAINER


class TrackPlaneUIDElement(Element):
	class_id = 0xE5
	class_name = 'TrackPlaneUID'
	class_parents = (TrackPlaneElement,)
	data_type = UINT


class TrackPlaneTypeElement(Element):
	class_id = 0xE6
	class_name = 'TrackPlaneType'
	class_parents = (TrackPlaneElement,)
	data_type = UINT


class TrackJoinBlocksElement(Element):
	class_id = 0xE9
	class_name = 'TrackJoinBlocks'
	class_parents = (TrackOperationElement,)
	data_type = CONTAINER


class TrackJoinUIDElement(Element):
	class_id = 0xED
	class_name = 'TrackJoinUID'
	class_parents = (TrackJoinBlocksElement,)
	data_type = UINT


class TrickTrackUIDElement(Element):
	class_id = 0xC0
	class_name = 'TrickTrackUID'
	class_parents = (TrackEntryElement,)
	data_type = UINT


class TrickTrackSegmentUIDElement(Element):
	class_id = 0xC1
	class_name = 'TrickTrackSegmentUID'
	class_parents = (TrackEntryElement,)
	data_type = BINARY


class TrickTrackFlagElement(Element):
	class_id = 0xC6
	class_name = 'TrickTrackFlag'
	class_parents = (TrackEntryElement,)
	data_type = UINT


class TrickMasterTrackUIDElement(Element):
	class_id = 0xC7
	class_name = 'TrickMasterTrackUID'
	class_parents = (TrackEntryElement,)
	data_type = UINT


class TrickMasterTrackSegmentUIDElement(Element):
	class_id = 0xC4
	class_name = 'TrickMasterTrackSegmentUID'
	class_parents = (TrackEntryElement,)
	data_type = BINARY


class ContentEncodingsElement(Element):
	class_id = 0x6D80
	class_name = 'ContentEncodings'
	class_parents = (TrackEntryElement,)
	data_type = CONTAINER


class ContentEncodingElement(Element):
	class_id = 0x6240
	class_name = 'ContentEncoding'
	class_parents = (ContentEncodingsElement,)
	data_type = CONTAINER


class ContentEncodingOrderElement(Element):
	class_id = 0x5031
	class_name = 'ContentEncodingOrder'
	class_parents = (ContentEncodingElement,)
	data_type = UINT


class ContentEncodingScopeElement(Element):
	class_id = 0x5032
	class_name = 'ContentEncodingScope'
	class_parents = (ContentEncodingElement,)
	data_type = UINT


class ContentEncodingTypeElement(Element):
	class_id = 0x5033
	class_name = 'ContentEncodingType'
	class_parents = (ContentEncodingElement,)
	data_type = UINT


class ContentCompressionElement(Element):
	class_id = 0x5034
	class_name = 'ContentCompression'
	class_parents = (ContentEncodingElement,)
	data_type = CONTAINER


class ContentCompAlgoElement(Element):
	class_id = 0x4254
	class_name = 'ContentCompAlgo'
	class_parents = (ContentCompressionElement,)
	data_type = UINT


class ContentCompSettingsElement(Element):
	class_id = 0x4255
	class_name = 'ContentCompSettings'
	class_parents = (ContentCompressionElement,)
	data_type = BINARY


class ContentEncryptionElement(Element):
	class_id = 0x5035
	class_name = 'ContentEncryption'
	class_parents = (ContentEncodingElement,)
	data_type = CONTAINER


class ContentEncAlgoElement(Element):
	class_id = 0x47E1
	class_name = 'ContentEncAlgo'
	class_parents = (ContentEncryptionElement,)
	data_type = UINT


class ContentEncKeyIDElement(Element):
	class_id = 0x47E2
	class_name = 'ContentEncKeyID'
	class_parents = (ContentEncryptionElement,)
	data_type = BINARY


class ContentSignatureElement(Element):
	class_id = 0x47E3
	class_name = 'ContentSignature'
	class_parents = (ContentEncryptionElement,)
	data_type = BINARY


class ContentSigKeyIDElement(Element):
	class_id = 0x47E4
	class_name = 'ContentSigKeyID'
	class_parents = (ContentEncryptionElement,)
	data_type = BINARY


class ContentSigAlgoElement(Element):
	class_id = 0x47E5
	class_name = 'ContentSigAlgo'
	class_parents = (ContentEncryptionElement,)
	data_type = UINT


class ContentSigHashAlgoElement(Element):
	class_id = 0x47E6
	class_name = 'ContentSigHashAlgo'
	class_parents = (ContentEncryptionElement,)
	data_type = UINT


class CuesElement(Element):
	class_id = 0x1c53bb6b
	class_name = 'Cues'
	class_parents = (SegmentElement,)
	data_type = CONTAINER


class CuePointElement(Element):
	class_id = 0xbb
	class_name = 'CuePoint'
	class_parents = (CuesElement,)
	data_type = CONTAINER


class CueTimeElement(Element):
	class_id = 0xb3
	class_name = 'CueTime'
	class_parents = (CuePointElement,)
	data_type = UINT


class CueTrackPositionsElement(Element):
	class_id = 0xb7
	class_name = 'CueTrackPositions'
	class_parents = (CuePointElement,)
	data_type = CONTAINER


class CueTrackElement(Element):
	class_id = 0xf7
	class_name = 'CueTrack'
	class_parents = (CueTrackPositionsElement,)
	data_type = UINT


class CueClusterPositionElement(Element):
	class_id = 0xf1
	class_name = 'CueClusterPosition'
	class_parents = (CueTrackPositionsElement,)
	data_type = UINT


class CueBlockNumberElement(Element):
	class_id = 0x5378
	class_name = 'CueBlockNumber'
	class_parents = (CueTrackPositionsElement,)
	data_type = UINT


class CueCodecStateElement(Element):
	class_id = 0xea
	class_name = 'CueCodecState'
	class_parents = (CueTrackPositionsElement,)
	data_type = UINT


class CueReferenceElement(Element):
	class_id = 0xdb
	class_name = 'CueReference'
	class_parents = (CueTrackPositionsElement,)
	data_type = CONTAINER


class CueRefTimeElement(Element):
	class_id = 0x96
	class_name = 'CueRefTime'
	class_parents = (CueReferenceElement,)
	data_type = UINT


class CueRefClusterElement(Element):
	class_id = 0x97
	class_name = 'CueRefCluster'
	class_parents = (CueReferenceElement,)
	data_type = UINT


class CueRefNumberElement(Element):
	class_id = 0x535f
	class_name = 'CueRefNumber'
	class_parents = (CueReferenceElement,)
	data_type = UINT


class CueRefCodecStateElement(Element):
	class_id = 0xeb
	class_name = 'CueRefCodecState'
	class_parents = (CueReferenceElement,)
	data_type = UINT


class AttachmentsElement(Element):
	class_id = 0x1941a469
	class_name = 'Attachments'
	class_parents = (SegmentElement,)
	data_type = CONTAINER


class AttachedFileElement(Element):
	class_id = 0x61a7
	class_name = 'AttachedFile'
	class_parents = (AttachmentsElement,)
	data_type = CONTAINER


class FileDescriptionElement(Element):
	class_id = 0x467e
	class_name = 'FileDescription'
	class_parents = (AttachedFileElement,)
	data_type = UNICODE


class FileNameElement(Element):
	class_id = 0x466e
	class_name = 'FileName'
	class_parents = (AttachedFileElement,)
	data_type = UNICODE


class FileMimeTypeElement(Element):
	class_id = 0x4660
	class_name = 'FileMimeType'
	class_parents = (AttachedFileElement,)
	data_type = STRING


class FileDataElement(Element):
	class_id = 0x465c
	class_name = 'FileData'
	class_parents = (AttachedFileElement,)
	data_type = BINARY


class FileUIDElement(Element):
	class_id = 0x46ae
	class_name = 'FileUID'
	class_parents = (AttachedFileElement,)
	data_type = UINT


class FileReferralElement(Element):
	class_id = 0x4675
	class_name = 'FileReferral'
	class_parents = (AttachedFileElement,)
	data_type = BINARY


class FileUsedStartTimeElement(Element):
	class_id = 0x4661
	class_name = 'FileUsedStartTime'
	class_parents = (AttachedFileElement,)
	data_type = UINT


class FileUsedEndTimeElement(Element):
	class_id = 0x4662
	class_name = 'FileUsedEndTime'
	class_parents = (AttachedFileElement,)
	data_type = UINT


class ChaptersElement(Element):
	class_id = 0x1043a770
	class_name = 'Chapters'
	class_parents = (SegmentElement,)
	data_type = CONTAINER


class EditionEntryElement(Element):
	class_id = 0x45b9
	class_name = 'EditionEntry'
	class_parents = (ChaptersElement,)
	data_type = CONTAINER


class EditionUIDElement(Element):
	class_id = 0x45bc
	class_name = 'EditionUID'
	class_parents = (EditionEntryElement,)
	data_type = UINT


class EditionFlagHiddenElement(Element):
	class_id = 0x45bd
	class_name = 'EditionFlagHidden'
	class_parents = (EditionEntryElement,)
	data_type = UINT


class EditionFlagDefaultElement(Element):
	class_id = 0x45db
	class_name = 'EditionFlagDefault'
	class_parents = (EditionEntryElement,)
	data_type = UINT


class EditionFlagOrderedElement(Element):
	class_id = 0x45dd
	class_name = 'EditionFlagOrdered'
	class_parents = (EditionEntryElement,)
	data_type = UINT


class ChapterAtomElement(Element):
	class_id = 0xb6
	class_name = 'ChapterAtom'
	class_parents = (EditionEntryElement, 'self')
	data_type = CONTAINER


class ChapterUIDElement(Element):
	class_id = 0x73c4
	class_name = 'ChapterUID'
	class_parents = (ChapterAtomElement,)
	data_type = UINT


class ChapterTimeStartElement(Element):
	class_id = 0x91
	class_name = 'ChapterTimeStart'
	class_parents = (ChapterAtomElement,)
	data_type = UINT


class ChapterTimeEndElement(Element):
	class_id = 0x92
	class_name = 'ChapterTimeEnd'
	class_parents = (ChapterAtomElement,)
	data_type = UINT


class ChapterFlagHiddenElement(Element):
	class_id = 0x98
	class_name = 'ChapterFlagHidden'
	class_parents = (ChapterAtomElement,)
	data_type = UINT


class ChapterFlagEnabledElement(Element):
	class_id = 0x4598
	class_name = 'ChapterFlagEnabled'
	class_parents = (ChapterAtomElement,)
	data_type = UINT


class ChapterSegmentUIDElement(Element):
	class_id = 0x6e67
	class_name = 'ChapterSegmentUID'
	class_parents = (ChapterAtomElement,)
	data_type = BINARY


class ChapterSegmentEditionUIDElement(Element):
	class_id = 0x6ebc
	class_name = 'ChapterSegmentEditionUID'
	class_parents = (ChapterAtomElement,)
	data_type = BINARY


class ChapterPhysicalEquivElement(Element):
	class_id = 0x63c3
	class_name = 'ChapterPhysicalEquiv'
	class_parents = (ChapterAtomElement,)
	data_type = UINT


class ChapterTrackElement(Element):
	class_id = 0x8f
	class_name = 'ChapterTrack'
	class_parents = (ChapterAtomElement,)
	data_type = CONTAINER


class ChapterTrackNumberElement(Element):
	class_id = 0x89
	class_name = 'ChapterTrackNumber'
	class_parents = (ChapterTrackElement,)
	data_type = UINT


class ChapterDisplayElement(Element):
	class_id = 0x80
	class_name = 'ChapterDisplay'
	class_parents = (ChapterAtomElement,)
	data_type = CONTAINER


class ChapStringElement(Element):
	class_id = 0x85
	class_name = 'ChapString'
	class_parents = (ChapterDisplayElement,)
	data_type = UNICODE


class ChapLanguageElement(Element):
	class_id = 0x437c
	class_name = 'ChapLanguage'
	class_parents = (ChapterDisplayElement,)
	data_type = STRING


class ChapCountryElement(Element):
	class_id = 0x437e
	class_name = 'ChapCountry'
	class_parents = (ChapterDisplayElement,)
	data_type = STRING


class ChapProcessElement(Element):
	class_id = 0x6944
	class_name = 'ChapProcess'
	class_parents = (ChapterAtomElement,)
	data_type = CONTAINER


class ChapProcessCodecIDElement(Element):
	class_id = 0x6955
	class_name = 'ChapProcessCodecID'
	class_parents = (ChapProcessElement,)
	data_type = UINT


class ChapProcessPrivateElement(Element):
	class_id = 0x450d
	class_name = 'ChapProcessPrivate'
	class_parents = (ChapProcessElement,)
	data_type = BINARY


class ChapProcessCommandElement(Element):
	class_id = 0x6911
	class_name = 'ChapProcessCommand'
	class_parents = (ChapProcessElement,)
	data_type = CONTAINER


class ChapProcessTimeElement(Element):
	class_id = 0x6922
	class_name = 'ChapProcessTime'
	class_parents = (ChapProcessCommandElement,)
	data_type = UINT


class ChapProcessDataElement(Element):
	class_id = 0x6933
	class_name = 'ChapProcessData'
	class_parents = (ChapProcessCommandElement,)
	data_type = BINARY


class TagsElement(Element):
	class_id = 0x1254c367
	class_name = 'Tags'
	class_parents = (SegmentElement,)
	data_type = CONTAINER


class TagElement(Element):
	class_id = 0x7373
	class_name = 'Tag'
	class_parents = (TagsElement,)
	data_type = CONTAINER


class TargetsElement(Element):
	class_id = 0x63c0
	class_name = 'Targets'
	class_parents = (TagElement,)
	data_type = CONTAINER


class TargetTypeValueElement(Element):
	class_id = 0x68ca
	class_name = 'TargetTypeValue'
	class_parents = (TargetsElement,)
	data_type = UINT


class TargetTypeElement(Element):
	class_id = 0x63ca
	class_name = 'TargetType'
	class_parents = (TargetsElement,)
	data_type = STRING


class TagTrackUIDElement(Element):
	class_id = 0x63c5
	class_name = 'TagTrackUID'
	class_parents = (TargetsElement,)
	data_type = UINT


class TagEditionUIDElement(Element):
	class_id = 0x63c9
	class_name = 'TagEditionUID'
	class_parents = (TargetsElement,)
	data_type = UINT


class TagChapterUIDElement(Element):
	class_id = 0x63c4
	class_name = 'TagChapterUID'
	class_parents = (TargetsElement,)
	data_type = UINT


class TagAttachmentUIDElement(Element):
	class_id = 0x63c6
	class_name = 'TagAttachmentUID'
	class_parents = (TargetsElement,)
	data_type = UINT


class SimpleTagElement(Element):
	class_id = 0x67c8
	class_name = 'SimpleTag'
	class_parents = (TagElement, 'self')
	data_type = CONTAINER


class TagNameElement(Element):
	class_id = 0x45a3
	class_name = 'TagName'
	class_parents = (SimpleTagElement,)
	data_type = UNICODE


class TagLanguageElement(Element):
	class_id = 0x447a
	class_name = 'TagLanguage'
	class_parents = (SimpleTagElement,)
	data_type = STRING


class TagDefaultElement(Element):
	class_id = 0x4484
	class_name = 'TagDefault'
	class_parents = (SimpleTagElement,)
	data_type = UINT


class TagStringElement(Element):
	class_id = 0x4487
	class_name = 'TagString'
	class_parents = (SimpleTagElement,)
	data_type = UNICODE


class TagBinaryElement(Element):
	class_id = 0x4485
	class_name = 'TagBinary'
	class_parents = (SimpleTagElement,)
	data_type = BINARY


class Matroska(EBML):
	elements = EBML.elements + (
		SegmentElement,
		SeekHeadElement,
		SeekElement,
		SeekIDElement,
		SeekPositionElement,
		InfoElement,
		SegmentUIDElement,
		SegmentFilenameElement,
		PrevUIDElement,
		PrevFilenameElement,
		NextUIDElement,
		NextFilenameElement,
		SegmentFamilyElement,
		ChapterTranslateElement,
		ChapterTranslateEditionUIDElement,
		ChapterTranslateCodecElement,
		ChapterTranslateIDElement,
		TimecodeScaleElement,
		DurationElement,
		DateUTCElement,
		TitleElement,
		MuxingAppElement,
		WritingAppElement,
		ClusterElement,
		TimecodeElement,
		SilentTracksElement,
		SilentTrackNumberElement,
		PositionElement,
		PrevSizeElement,
		SimpleBlockElement,
		BlockGroupElement,
		BlockElement,
		BlockVirtualElement,
		BlockAdditionsElement,
		BlockMoreElement,
		BlockAddIDElement,
		BlockAdditionalElement,
		BlockDurationElement,
		ReferencePriorityElement,
		ReferenceBlockElement,
		ReferenceVirtualElement,
		CodecStateElement,
		SlicesElement,
		TimeSliceElement,
		LaceNumberElement,
		FrameNumberElement,
		BlockAdditionIDElement,
		DelayElement,
		SliceDurationElement,
		ReferenceFrameElement,
		ReferenceOffsetElement,
		ReferenceTimeCodeElement,
		EncryptedBlockElement,
		TracksElement,
		TrackEntryElement,
		TrackNumberElement,
		TrackUIDElement,
		TrackTypeElement,
		FlagEnabledElement,
		FlagDefaultElement,
		FlagForcedElement,
		FlagLacingElement,
		MinCacheElement,
		MaxCacheElement,
		DefaultDurationElement,
		TrackTimecodeScaleElement,
		TrackOffsetElement,
		MaxBlockAdditionIDElement,
		NameElement,
		LanguageElement,
		CodecIDElement,
		CodecPrivateElement,
		CodecNameElement,
		AttachmentLinkElement,
		CodecSettingsElement,
		CodecInfoURLElement,
		CodecDownloadURLElement,
		CodecDecodeAllElement,
		TrackOverlayElement,
		TrackTranslateElement,
		TrackTranslateEditionUIDElement,
		TrackTranslateCodecElement,
		TrackTranslateTrackIDElement,
		VideoElement,
		FlagInterlacedElement,
		StereoModeElement,
		OldStereoModeElement,
		PixelWidthElement,
		PixelHeightElement,
		PixelCropBottomElement,
		PixelCropTopElement,
		PixelCropLeftElement,
		PixelCropRightElement,
		DisplayWidthElement,
		DisplayHeightElement,
		DisplayUnitElement,
		AspectRatioTypeElement,
		ColourSpaceElement,
		GammaValueElement,
		FrameRateElement,
		AudioElement,
		SamplingFrequencyElement,
		OutputSamplingFrequencyElement,
		ChannelsElement,
		ChannelPositionsElement,
		BitDepthElement,
		TrackOperationElement,
		TrackCombinePlanesElement,
		TrackPlaneElement,
		TrackPlaneUIDElement,
		TrackPlaneTypeElement,
		TrackJoinBlocksElement,
		TrackJoinUIDElement,
		TrickTrackUIDElement,
		TrickTrackSegmentUIDElement,
		TrickTrackFlagElement,
		TrickMasterTrackUIDElement,
		TrickMasterTrackSegmentUIDElement,
		ContentEncodingsElement,
		ContentEncodingElement,
		ContentEncodingOrderElement,
		ContentEncodingScopeElement,
		ContentEncodingTypeElement,
		ContentCompressionElement,
		ContentCompAlgoElement,
		ContentCompSettingsElement,
		ContentEncryptionElement,
		ContentEncAlgoElement,
		ContentEncKeyIDElement,
		ContentSignatureElement,
		ContentSigKeyIDElement,
		ContentSigAlgoElement,
		ContentSigHashAlgoElement,
		CuesElement,
		CuePointElement,
		CueTimeElement,
		CueTrackPositionsElement,
		CueTrackElement,
		CueClusterPositionElement,
		CueBlockNumberElement,
		CueCodecStateElement,
		CueReferenceElement,
		CueRefTimeElement,
		CueRefClusterElement,
		CueRefNumberElement,
		CueRefCodecStateElement,
		AttachmentsElement,
		AttachedFileElement,
		FileDescriptionElement,
		FileNameElement,
		FileMimeTypeElement,
		FileDataElement,
		FileUIDElement,
		FileReferralElement,
		FileUsedStartTimeElement,
		FileUsedEndTimeElement,
		ChaptersElement,
		EditionEntryElement,
		EditionUIDElement,
		EditionFlagHiddenElement,
		EditionFlagDefaultElement,
		EditionFlagOrderedElement,
		ChapterAtomElement,
		ChapterUIDElement,
		ChapterTimeStartElement,
		ChapterTimeEndElement,
		ChapterFlagHiddenElement,
		ChapterFlagEnabledElement,
		ChapterSegmentUIDElement,
		ChapterSegmentEditionUIDElement,
		ChapterPhysicalEquivElement,
		ChapterTrackElement,
		ChapterTrackNumberElement,
		ChapterDisplayElement,
		ChapStringElement,
		ChapLanguageElement,
		ChapCountryElement,
		ChapProcessElement,
		ChapProcessCodecIDElement,
		ChapProcessPrivateElement,
		ChapProcessCommandElement,
		ChapProcessTimeElement,
		ChapProcessDataElement,
		TagsElement,
		TagElement,
		TargetsElement,
		TargetTypeValueElement,
		TargetTypeElement,
		TagTrackUIDElement,
		TagEditionUIDElement,
		TagChapterUIDElement,
		TagAttachmentUIDElement,
		SimpleTagElement,
		TagNameElement,
		TagLanguageElement,
		TagDefaultElement,
		TagStringElement,
		TagBinaryElement
	)