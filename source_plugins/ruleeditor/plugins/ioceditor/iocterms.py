schemas = """{http://openioc.org/schemas/OpenIOC_1.1}"""
iocterms="""
<!--
    TITLE:          current.iocterms
    VERSION:        1.1 (draft)
    DESCRIPTION:    Terms available for OpenIOC 1.1.  These can be used, out of the box, with IOCe.
    LICENSE:        Copyright 2013 Mandiant Corporation.  Licensed under the Apache 2.0 license.

    Mandiant licenses this file to you under the Apache License, Version
    2.0 (the "License"); you may not use this file except in compliance with the
    License.  You may obtain a copy of the License at:

            http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
    implied.  See the License for the specific language governing
    permissions and limitations under the License.
-->
<ioctermlist xmlns="http://openioc.org/schemas/OpenIOC_1.1" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" last-modified="2013-05-14T16:15:00Z">
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ArpEntryItem/CacheType" title="ARP Cache Type" />
  <iocterm data-type="xs:string" display-type="IP" term-source="application/vnd.mandiant.mir" text="ArpEntryItem/IPv4Address" title="ARP IPv4 Address" />
  <iocterm data-type="xs:string" display-type="IP" term-source="application/vnd.mandiant.mir" text="ArpEntryItem/Interface" title="ARP Interface" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ArpEntryItem/PhysicalAddress" title="ARP Physical Address" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="CookieHistoryItem/BrowserName" title="CookieHistory Browser Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="CookieHistoryItem/BrowserVersion" title="CookieHistory Browser Version" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="CookieHistoryItem/CookieFlags" title="CookieHistory Cookie Flags" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="CookieHistoryItem/CookieName" title="CookieHistory Cookie Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="CookieHistoryItem/CookiePath" title="CookieHistory Cookie Path" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="CookieHistoryItem/CookieValue" title="CookieHistory Cookie Value" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="CookieHistoryItem/CreationDate" title="CookieHistory Creation Date" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="CookieHistoryItem/ExpirationDate" title="CookieHistory Expiration Date" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="CookieHistoryItem/FileName" title="CookieHistory File Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="CookieHistoryItem/FilePath" title="CookieHistory File Path" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="CookieHistoryItem/HostName" title="CookieHistory Host Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="CookieHistoryItem/IsHttpOnly" title="CookieHistory IsHttpOnly" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="CookieHistoryItem/IsSecure" title="CookieHistory IsSecure" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="CookieHistoryItem/LastAccessedDate" title="CookieHistory Last Accessed Date" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="CookieHistoryItem/LastModifiedDate" title="CookieHistory Last Modified Date" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="CookieHistoryItem/Profile" title="CookieHistory Profile" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="CookieHistoryItem/Username" title="CookieHistory Username" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DiskItem/DiskName" title="Disk Name" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="DiskItem/DiskSize" title="Disk Size" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="DiskItem/PartitionList/Partition/PartitionLength" title="Disk Partition Length" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="DiskItem/PartitionList/Partition/PartitionNumber" title="Disk Partition Number" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="DiskItem/PartitionList/Partition/PartitionOffset" title="Disk Partition Offset" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DiskItem/PartitionList/Partition/PartitionType" title="Disk Partition Type" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="DnsEntryItem/DataLength" title="DNS Data Length" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DnsEntryItem/Flags" title="DNS Flags" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DnsEntryItem/Host" title="DNS Host" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DnsEntryItem/RecordData/Host" title="DNS Record Data Host" />
  <iocterm data-type="xs:string" display-type="IP" term-source="application/vnd.mandiant.mir" text="DnsEntryItem/RecordData/IPv4Address" title="DNS Record Data IPv4 Address" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DnsEntryItem/RecordName" title="DNS Record Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DnsEntryItem/RecordType" title="DNS Record Type" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DnsEntryItem/TimeToLive" title="DNS Time To Live" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/CertificateIssuer" title="Driver Certificate Issuer" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/CertificateSubject" title="Driver Certificate Subject" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/DeviceItem/AttachedDeviceName" title="Driver Attached Device Name" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="DriverItem/DeviceItem/AttachedDeviceObject" title="Driver Attached Device Object" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/DeviceItem/AttachedDriverName" title="Driver Attached Driver Name" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="DriverItem/DeviceItem/AttachedDriverObject" title="Driver Attached Driver Object" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/DeviceItem/AttachedToDeviceName" title="Driver Attached To Device Name" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="DriverItem/DeviceItem/AttachedToDeviceObject" title="Driver Attached To Device Object" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/DeviceItem/AttachedToDriverName" title="Driver Attached To Driver Name" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="DriverItem/DeviceItem/AttachedToDriverObject" title="Driver Attached To Driver Object" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/DeviceItem/DeviceName" title="Driver Device Name" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="DriverItem/DeviceItem/DeviceObject" title="Driver Device Object" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/DeviceItem/DriverName" title="Driver Device Driver Name" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="DriverItem/DriverInit" title="Driver Init" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/DriverName" title="Driver Name" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="DriverItem/DriverObjectAddress" title="Driver Object Address" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="DriverItem/DriverStartIo" title="Driver StartIo" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="DriverItem/DriverUnload" title="Driver Unload" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="DriverItem/ImageBase" title="Driver Image Base" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="DriverItem/ImageSize" title="Driver Image Size" />
  <iocterm data-type="xs:string" display-type="md5" term-source="application/vnd.mandiant.mir" text="DriverItem/Md5sum" title="Driver Md5sum" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/BaseAddress" title="Driver PEInfo Base Address" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/DetectedAnomalies/string" title="Driver PEInfo Detected Anomalies" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/DetectedEntryPointSignature/Name" title="Driver PEInfo Detected Entry Point Signature Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/DetectedEntryPointSignature/Type" title="Driver PEInfo Detected Entry Point Signature Type" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/DigitalSignature/CertificateIssuer" title="Driver Certificate Issuer" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/DigitalSignature/CertificateSubject" title="Driver Certificate Subject" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/DigitalSignature/Description" title="Driver Signature Description" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/DigitalSignature/SignatureExists" title="Driver Signature Exists" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/DigitalSignature/SignatureVerified" title="Driver Signature Verified" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/EpJumpCodes/Depth" title="Driver PEInfo EpJumpCodes Depth" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/EpJumpCodes/Opcodes" title="Driver PEInfo EpJumpCodes Opcodes" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/Exports/ExportedFunctions/string" title="Driver Exported Function" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/Exports/ExportsTimeStamp" title="Driver Exports Time Stamp" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/Exports/DllName" title="Driver Exports Dll Name" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/Exports/NumberOfFunctions" title="Driver Number Of Functions" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/Exports/NumberOfNames" title="Driver Number Of Names" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/ExtraneousBytes" title="Driver PEInfo Extraneous Bytes" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/ImportedModules/Module/ImportedFunctions/string" title="Driver Imported Function" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/ImportedModules/Module/Name" title="Driver Imported Module Name" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/PEChecksum/PEComputedAPI" title="Driver PEInfo PEChecksum PEComputedAPI" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/PEChecksum/PEFileAPI" title="Driver PEInfo PEChecksum PEFileAPI" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/PEChecksum/PEFileRaw" title="Driver PEInfo PEChecksum PEFileRaw" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/PETimeStamp" title="Driver PEInfo PETimeStamp" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/Sections/Section/DetectedCharacteristics" title="Driver PEInfo Sections Section Detected Characteristics" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/Sections/Section/DetectedSignatureKeys/string" title="Driver PEInfo Sections Section Detected Signature Keys" />
  <iocterm data-type="xs:string" display-type="float" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/Sections/Section/Entropy/CurveData/float" title="Driver PEInfo Sections Section Entropy CurveData float" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/Sections/Section/Name" title="Driver PEInfo Sections Section Name" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/Sections/Section/SizeInBytes" title="Driver PEInfo Sections Section Size" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/Sections/Section/Type" title="Driver PEInfo Sections Section Type" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/Subsystem" title="Driver PEInfo Subsystem" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/PEInfo/Type" title="Driver PEInfo Type" />
  <iocterm data-type="xs:string" display-type="sha1" term-source="application/vnd.mandiant.mir" text="DriverItem/Sha1sum" title="Driver Sha1sum" />
  <iocterm data-type="xs:string" display-type="sha256" term-source="application/vnd.mandiant.mir" text="DriverItem/Sha256sum" title="Driver Sha256sum" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/SignatureDescription" title="Driver Signature Description" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="DriverItem/SignatureExists" title="Driver Signature Exists" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="DriverItem/SignatureVerified" title="Driver Signature Verified" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="DriverItem/StringList/string" title="Driver String" />
  <iocterm data-type="xs:string" display-type="string" text="Email/Attachment/Content" title="Email attachment content" />
  <iocterm data-type="xs:string" display-type="string" text="Email/Attachment/MIMEType" title="Email Attachment MIME Type" />
  <iocterm data-type="xs:string" display-type="string" text="Email/Attachment/Name" title="Email Attachment Name" />
  <iocterm data-type="xs:int" display-type="int" text="Email/Attachment/SizeInBytes" title="Email Attachment Size" />
  <iocterm data-type="xs:int" display-type="int" text="Email/AttachmentCount" title="Email Attachment Count" />
  <iocterm data-type="xs:string" display-type="string" text="Email/BCC" title="Email BCC Recipient(s)" />
  <iocterm data-type="xs:string" display-type="string" text="Email/Body" title="Email Body Text" />
  <iocterm data-type="xs:string" display-type="string" text="Email/CC" title="Email CC Recipients(s)" />
  <iocterm data-type="xs:string" display-type="string" text="Email/Content-Type" title="Email Content-Type" />
  <iocterm data-type="xs:dateTime" display-type="date" text="Email/Date" title="Email Date (Sent)" />
  <iocterm data-type="xs:string" display-type="string" text="Email/From" title="Email Sender" />
  <iocterm data-type="xs:string" display-type="string" text="Email/In-Reply-To" title="Email In-Reply-To" />
  <iocterm data-type="xs:string" display-type="string" text="Email/MIME-Version" title="Email MIME-Version" />
  <iocterm data-type="xs:string" display-type="string" text="Email/Received" title="Email Received Date" />
  <iocterm data-type="xs:string" display-type="string" text="Email/ReceivedFromHost" title="Email Received From Host" />
  <iocterm data-type="xs:string" display-type="IP" text="Email/ReceivedFromIP" title="Email Received From IP" />
  <iocterm data-type="xs:string" display-type="string" text="Email/References" title="Email References" />
  <iocterm data-type="xs:string" display-type="string" text="Email/Return-Path" title="Email Return Path" />
  <iocterm data-type="xs:string" display-type="string" text="Email/Subject" title="Email Subject" />
  <iocterm data-type="xs:string" display-type="string" text="Email/Thread-Index" title="Email Thread-Index" />
  <iocterm data-type="xs:string" display-type="string" text="Email/Thread-Topic" title="Email Thread-Topic" />
  <iocterm data-type="xs:string" display-type="string" text="Email/To" title="Email Recipients" />
  <iocterm data-type="xs:string" display-type="string" text="Email/X-MS-Has-Attach" title="Email X-MS-Has-Attach" />
  <iocterm data-type="xs:string" display-type="string" text="Email/X-filenames" title="Email X-filenames" />
  <iocterm data-type="xs:int" display-type="int" text="Email/X-filesizes" title="Email X-filesizes" />
  <iocterm data-type="xs:string" display-type="string" text="Email/X-filetypes" title="Email X-filetypes" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="EventLogItem/CorrelationActivityId" title="EventLog Correlation Activity Id" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="EventLogItem/CorrelationRelatedActivityId" title="EventLog Correlation Related Activity Id" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="EventLogItem/EID" title="EventLog ID" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="EventLogItem/ExecutionProcessId" title="EventLog Execution Process Id" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="EventLogItem/ExecutionThreadId" title="EventLog Execution Thread Id" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="EventLogItem/blob" title="EventLog blob" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="EventLogItem/category" title="EventLog category" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="EventLogItem/categoryNum" title="EventLog categoryNum" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="EventLogItem/genTime" title="EventLog GenTime" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="EventLogItem/index" title="EventLog index" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="EventLogItem/log" title="EventLog log" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="EventLogItem/machine" title="EventLog machine" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="EventLogItem/message" title="EventLog Message" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="EventLogItem/reserved" title="EventLog reserved" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="EventLogItem/source" title="EventLog source" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="EventLogItem/type" title="EventLog type" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="EventLogItem/unformattedMessage/string" title="EventLog unformatted Message" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="EventLogItem/user" title="EventLog user" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="EventLogItem/writeTime" title="EventLog writeTime" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileDownloadHistoryItem/AutoResume" title="FileDownloadHistory AutoResume" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileDownloadHistoryItem/BrowserName" title="FileDownloadHistory Browser Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileDownloadHistoryItem/BrowserVersion" title="FileDownloadHistory Browser Version" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="FileDownloadHistoryItem/BytesDownloaded" title="FileDownloadHistory Bytes Downloaded" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileDownloadHistoryItem/CacheFlags" title="FileDownloadHistory Cache Flags" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="FileDownloadHistoryItem/CacheHitCount" title="FileDownloadHistory Cache Hit Count" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileDownloadHistoryItem/DownloadType" title="FileDownloadHistory Download Type" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="FileDownloadHistoryItem/EndDate" title="FileDownloadHistory End Date" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileDownloadHistoryItem/FileName" title="FileDownloadHistory File Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileDownloadHistoryItem/FullHttpHeader" title="FileDownloadHistory Full Http Header" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="FileDownloadHistoryItem/LastAccessedDate" title="FileDownloadHistory Last Accessed Date" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="FileDownloadHistoryItem/LastCacheSynchDate" title="FileDownloadHistory Last Cache Synch Date" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="FileDownloadHistoryItem/LastCheckedDate" title="FileDownloadHistory Last Checked Date" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="FileDownloadHistoryItem/LastModifiedDate" title="FileDownloadHistory Last Modified Date" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="FileDownloadHistoryItem/MaxBytes" title="FileDownloadHistory Max Bytes" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileDownloadHistoryItem/MimeType" title="FileDownloadHistory MimeType" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileDownloadHistoryItem/Profile" title="FileDownloadHistory Profile" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileDownloadHistoryItem/Referrer" title="FileDownloadHistory Referrer" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileDownloadHistoryItem/SourceURL" title="FileDownloadHistory Source URL" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="FileDownloadHistoryItem/StartDate" title="FileDownloadHistory Start Date" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileDownloadHistoryItem/State" title="FileDownloadHistory State" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileDownloadHistoryItem/TargetDirectory" title="FileDownloadHistory Target Directory" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileDownloadHistoryItem/TemporaryPath" title="FileDownloadHistory Temporary Path" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileDownloadHistoryItem/Username" title="FileDownloadHistory Username" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="FileItem/Accessed" title="File Accessed Time" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="FileItem/Changed" title="File Changed Time" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="FileItem/Created" title="File Created Time" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/DevicePath" title="File DevicePath" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/Drive" title="File Drive" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/FileAttributes" title="File Attribute" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/FileExtension" title="File Extension" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/FileName" title="File Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/FilePath" title="File Path" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="FileItem/FilenameAccessed" title="File Filename Accessed" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="FileItem/FilenameChanged" title="File Filename Changed" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="FileItem/FilenameCreated" title="File Filename Created" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="FileItem/FilenameModified" title="File Filename Modified" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/FullPath" title="File Full Path" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="FileItem/INode" title="File INode" />
  <iocterm data-type="xs:string" display-type="md5" term-source="application/vnd.mandiant.mir" text="FileItem/Md5sum" title="File MD5" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="FileItem/Modified" title="File Modified Time" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/detectedAnomaly" title="File detectedAnomaly" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/BaseAddress" title="File Base Address" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/DetectedAnomalies/string" title="File PE Detected Anomalies" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/DetectedEntryPointSignature/Name" title="File EntryPoint Sig Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/DetectedEntryPointSignature/Type" title="File EntryPoint Sig Type" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/DigitalSignature/CertificateIssuer" title="File Certificate Issuer" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/DigitalSignature/CertificateSubject" title="File Certificate Subject" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/DigitalSignature/Description" title="File Digital Signature Description" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/DigitalSignature/SignatureExists" title="File Digital Signature Exists" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/DigitalSignature/SignatureVerified" title="File Digital Signature Verified" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/EpJumpCodes/Depth" title="File Double Jump" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/EpJumpCodes/Opcodes" title="File PEInfo EpJumpCodes Opcodes" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/Exports/DllName" title="File Dll Export Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/Exports/ExportedFunctions/string" title="File Export Function" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/Exports/ExportsTimeStamp" title="File Exports Time Stamp" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/Exports/NumberOfFunctions" title="File Export Count" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/Exports/NumberOfNames" title="File Export Number Of Names" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/ExtraneousBytes" title="File Extraneous Bytes" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/ImportedModules/Module/ImportedFunctions/string" title="File Import Function" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/ImportedModules/Module/Name" title="File Import Name" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/ImportedModules/Module/NumberOfFunctions" title="File Number of Imported Functions" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/PEChecksum/PEComputedAPI" title="File PEComputedAPI" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/PEChecksum/PEFileAPI" title="File PE Checksum API" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/PEChecksum/PEFileRaw" title="File PEFileRaw" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/PETimeStamp" title="File Compile Time" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/ResourceInfoList/ResourceInfoItem/Data" title="File PEInfo Resource Info Data" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/ResourceInfoList/ResourceInfoItem/Language" title="File PEInfo Resource Info Language" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/ResourceInfoList/ResourceInfoItem/Name" title="File PEInfo Resource Info Name" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/ResourceInfoList/ResourceInfoItem/Size" title="File PEInfo Resource Info Size" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/ResourceInfoList/ResourceInfoItem/Type" title="File PEInfo Resource Info Type" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/Sections/NumberOfSections" title="File PEInfo Number of Sections" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/Sections/ActualNumberOfSections" title="File PEInfo Actual Number of Sections" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/Sections/Section/DetectedCharacteristics" title="File Detected Characteristics" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/Sections/Section/DetectedSignatureKeys/string" title="File Detected Signatures" />
  <iocterm data-type="xs:string" display-type="float" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/Sections/Section/Entropy/CurveData/float" title="File PEInfo Sections Section Entropy CurveData float" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/Sections/Section/Name" title="File Section Name" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/Sections/Section/SizeInBytes" title="File PE Section Size" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/Sections/Section/Type" title="File PE Section Type" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/Subsystem" title="File PE Subsystem" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/Type" title="File PE Type" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/VersionInfoList/VersionInfoItem/Comments" title="File PEInfo Version Info Comments" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/VersionInfoList/VersionInfoItem/CompanyName" title="File PEInfo Version Info CompanyName" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/VersionInfoList/VersionInfoItem/FileDescription" title="File PEInfo Version Info FileDescription" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/VersionInfoList/VersionInfoItem/FileVersion" title="File PEInfo Version Info FileVersion" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/VersionInfoList/VersionInfoItem/InternalName" title="File PEInfo Version Info InternalName" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/VersionInfoList/VersionInfoItem/Language" title="File PEInfo Version Info Language" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/VersionInfoList/VersionInfoItem/LegalCopyright" title="File PEInfo Version Info LegalCopyright" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/VersionInfoList/VersionInfoItem/LegalTrademarks" title="File PEInfo Version Info LegalTrademarks" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/VersionInfoList/VersionInfoItem/OriginalFilename" title="File PEInfo Version Info OriginalFilename" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/VersionInfoList/VersionInfoItem/PrivateBuild" title="File PEInfo Version Info PrivateBuild" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/VersionInfoList/VersionInfoItem/ProductName" title="File PEInfo Version Info ProductName" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/VersionInfoList/VersionInfoItem/ProductVersion" title="File PEInfo Version Info ProductVersion" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/PEInfo/VersionInfoList/VersionInfoItem/SpecialBuild" title="File PEInfo Version Info SpecialBuild" />
  <iocterm data-type="xs:string" display-type="float" term-source="application/vnd.mandiant.mir" text="FileItem/PeakCodeEntropy" title="File Peak Code Entropy" />
  <iocterm data-type="xs:string" display-type="float" term-source="application/vnd.mandiant.mir" text="FileItem/PeakEntropy" title="File Peak Entropy" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/SecurityID" title="File Security ID" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/SecurityType" title="File Security Type" />
  <iocterm data-type="xs:string" display-type="sha1" term-source="application/vnd.mandiant.mir" text="FileItem/Sha1sum" title="File Sha1sum" />
  <iocterm data-type="xs:string" display-type="sha256" term-source="application/vnd.mandiant.mir" text="FileItem/Sha256sum" title="File Sha256sum" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="FileItem/SizeInBytes" title="File Size" />
  <iocterm data-type="xs:string" display-type="md5" term-source="application/vnd.mandiant.mir" text="FileItem/StreamList/Stream/Md5sum" title="File ADS MD5" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/StreamList/Stream/Name" title="File ADS Name" />
  <iocterm data-type="xs:string" display-type="sha1" term-source="application/vnd.mandiant.mir" text="FileItem/StreamList/Stream/Sha1sum" title="File Stream Sha1sum" />
  <iocterm data-type="xs:string" display-type="sha256" term-source="application/vnd.mandiant.mir" text="FileItem/StreamList/Stream/Sha256sum" title="File Stream Sha256sum" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="FileItem/StreamList/Stream/SizeInBytes" title="File ADS Size" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/StringList/string" title="File Strings" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FileItem/Username" title="File Owner" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FormHistoryItem/BrowserName" title="FormHistory Browser Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FormHistoryItem/BrowserVersion" title="FormHistory Browser Version" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="FormHistoryItem/CreationDate" title="FormHistory Creation Date" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FormHistoryItem/EncryptedPassword" title="FormHistory Encrypted Password" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FormHistoryItem/EncryptionType" title="FormHistory Encryption Type" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="FormHistoryItem/FirstUsedDate" title="FormHistory First Used Date" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FormHistoryItem/FormFieldName" title="FormHistory Form Field Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FormHistoryItem/FormFieldValue" title="FormHistory Form Field Value" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FormHistoryItem/FormSubmitURL" title="FormHistory Form Submit URL" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FormHistoryItem/FormType" title="FormHistory Form Type" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FormHistoryItem/Guid" title="FormHistory Guid" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FormHistoryItem/HostName" title="FormHistory Host Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FormHistoryItem/HttpRealm" title="FormHistory Http Realm" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="FormHistoryItem/LastUsedDate" title="FormHistory Last Used Date" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FormHistoryItem/PasswordFieldName" title="FormHistory Password Field Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FormHistoryItem/Profile" title="FormHistory Profile" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="FormHistoryItem/TimesUsed" title="FormHistory Times Used" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FormHistoryItem/Username" title="FormHistory Username" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FormHistoryItem/UsernameFieldName" title="FormHistory Username Field Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="FormHistoryItem/UsernameFieldValue" title="FormHistory Username Field Value" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="HiveItem/Name" title="Hive Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="HiveItem/Path" title="Hive Path" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="HookItem/DigitalSignatureHooked/CertificateIssuer" title="Hook Digital Signature Hooked Certificate Issuer" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="HookItem/DigitalSignatureHooked/CertificateSubject" title="Hook Digital Signature Hooked Certificate Subject" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="HookItem/DigitalSignatureHooked/Description" title="Hook Digital Signature Hooked Description" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="HookItem/DigitalSignatureHooked/SignatureExists" title="Hook Digital Signature Hooked Signature Exists" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="HookItem/DigitalSignatureHooked/SignatureVerified" title="Hook Digital Signature Hooked Signature Verified" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="HookItem/DigitalSignatureHooking/CertificateIssuer" title="Hook Digital Signature Hooking Certificate Issuer" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="HookItem/DigitalSignatureHooking/CertificateSubject" title="Hook Digital Signature Hooking Certificate Subject" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="HookItem/DigitalSignatureHooking/Description" title="Hook Digital Signature Hooking Description" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="HookItem/DigitalSignatureHooking/SignatureExists" title="Hook Digital Signature Hooking Signature Exists" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="HookItem/DigitalSignatureHooking/SignatureVerified" title="Hook Digital Signature Hooking Signature Verified" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="HookItem/HookDescription" title="Hook Description" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="HookItem/HookedFunction" title="Hook Hooked Function" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="HookItem/HookedModule" title="Hook Hooked Module" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="HookItem/HookingAddress" title="Hook Hooking Address" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="HookItem/HookingModule" title="Hook Hooking Module" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="ModuleItem/ModuleAddress" title="Module Address" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="ModuleItem/ModuleBase" title="Module Base" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="ModuleItem/ModuleInit" title="Module Init" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ModuleItem/ModuleName" title="Module Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ModuleItem/ModulePath" title="Module Path" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="ModuleItem/ModuleSize" title="Module Size" />
  <iocterm data-type="xs:string" display-type="string" text="Network/DNS" title="Network DNS" />
  <iocterm data-type="xs:string" display-type="string" text="Network/HTTP_Referr" title="Network String HTTP Referr" />
  <iocterm data-type="xs:string" display-type="string" text="Network/String" title="Network String General" />
  <iocterm data-type="xs:string" display-type="string" text="Network/URI" title="Network String URI" />
  <iocterm data-type="xs:string" display-type="string" text="Network/UserAgent" title="Network String User Agent" />
  <iocterm data-type="xs:dateTime" display-type="date" text="PortItem/CreationTime" title="Port Creation Time" />
  <iocterm data-type="xs:string" display-type="IP" term-source="application/vnd.mandiant.mir" text="PortItem/localIP" title="Port Local IP" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="PortItem/localPort" title="Port Local Port" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="PortItem/path" title="Port Path" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="PortItem/pid" title="Port PID" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="PortItem/process" title="Port Process" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="PortItem/protocol" title="Port Protocol" />
  <iocterm data-type="xs:string" display-type="IP" term-source="application/vnd.mandiant.mir" text="PortItem/remoteIP" title="Port Remote IP" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="PortItem/remotePort" title="Port Remote Port" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="PortItem/state" title="Port State" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="PrefetchItem/AccessedFileList/AccessedFile" title="Prefetch Accessed File" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="PrefetchItem/ApplicationFileName" title="Prefetch File Executed" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="PrefetchItem/ApplicationFullPath" title="Prefetch Application Full Path" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="PrefetchItem/Created" title="Prefetch File Created" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="PrefetchItem/FullPath" title="Prefetch Full Path" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="PrefetchItem/LastRun" title="Prefetch Last Run" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="PrefetchItem/PrefetchHash" title="Prefetch Hash" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="PrefetchItem/VolumeList/VolumeItem/DevicePath" title="Prefetch Volume Device Path" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="PrefetchItem/VolumeList/VolumeItem/CreationTime" title="Prefetch Volume Creation Time" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="PrefetchItem/VolumeList/VolumeItem/SerialNumber" title="Prefetch Volume Serial Number" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="PrefetchItem/ReportedSizeInBytes" title="Prefetch Reported Size" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="PrefetchItem/SizeInBytes" title="Prefetch Size" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="PrefetchItem/TimesExecuted" title="Prefetch Times Executed" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/HandleList/Handle/AccessMask" title="Process Handle Access Mask" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="ProcessItem/HandleList/Handle/HandleCount" title="Process Handle Count" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="ProcessItem/HandleList/Handle/Index" title="Process Handle Index" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/HandleList/Handle/Name" title="Process Handle Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/HandleList/Handle/ObjectAddress" title="Process Handle Object Address" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/HandleList/Handle/PointerCount" title="Process Handle Pointer Count" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/HandleList/Handle/Type" title="Process Handle Type" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="ProcessItem/PortList/PortItem/CreationTime" title="Process Port Creation Time" />
  <iocterm data-type="xs:string" display-type="IP" term-source="application/vnd.mandiant.mir" text="ProcessItem/PortList/PortItem/localIP" title="Process Port Local IP" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="ProcessItem/PortList/PortItem/localPort" title="Process Local Port" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/PortList/PortItem/path" title="Process Port Path" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="ProcessItem/PortList/PortItem/pid" title="Process Port PID" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/PortList/PortItem/process" title="Process Port Process" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/PortList/PortItem/protocol" title="Process Port Protocol" />
  <iocterm data-type="xs:string" display-type="IP" term-source="application/vnd.mandiant.mir" text="ProcessItem/PortList/PortItem/remoteIP" title="Process Port Remote IP" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="ProcessItem/PortList/PortItem/remotePort" title="Process Remote Port" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/PortList/PortItem/state" title="Process State" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/DigitalSignature/CertificateIssuer" title="Process Section Certificate Issuer" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/DigitalSignature/CertificateSubject" title="Process Section Certificate Subject" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/DigitalSignature/Description" title="Process Section Signature Description" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/DigitalSignature/SignatureExists" title="Process Section Signature Exists" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/DigitalSignature/SignatureVerified" title="Process Section Signature Verified" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/Injected" title="Process Section Injected" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/Mapped" title="Process Mapped" />
  <iocterm data-type="xs:string" display-type="md5" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/Md5sum" title="Process Section MD5" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/Name" title="Process Section Name" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/BaseAddress" title="Process SectionList MemorySection PEInfo Base Address" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/DetectedAnomalies/string" title="Process SectionList MemorySection PEInfo Detected Anomalies" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/DetectedEntryPointSignature/Name" title="Process SectionList MemorySection PEInfo Detected EntryPoint Signature Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/DetectedEntryPointSignature/Type" title="Process SectionList MemorySection PEInfo Detected EntryPoint Signature Type" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/DigitalSignature/CertificateIssuer" title="Process SectionList MemorySection PEInfo Digital Signature Certificate Issuer" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/DigitalSignature/CertificateSubject" title="Process SectionList MemorySection PEInfo Digital Signature Certificate Subject" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/DigitalSignature/Description" title="Process SectionList MemorySection PEInfo Digital Signature Description" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/DigitalSignature/SignatureExists" title="Process SectionList MemorySection PEInfo Digital Signature Signature Exists" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/DigitalSignature/SignatureVerified" title="Process SectionList MemorySection PEInfo Digital Signature Signature Verified" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/EpJumpCodes/Depth" title="Process SectionList MemorySection PEInfo EpJumpCodes Depth" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/EpJumpCodes/Opcodes" title="Process SectionList MemorySection PEInfo EpJumpCodes Opcodes" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/Exports/ExportedFunctions/string" title="Process Section Exported Function" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/Exports/ExportsTimeStamp" title="Process Section Exports Time Stamp" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/Exports/NumberOfFunctions" title="Process Section Number Of Functions" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/Exports/NumberOfNames" title="Process Section Export Number Of Names" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/ExtraneousBytes" title="Process SectionList MemorySection PEInfo Extraneous Bytes" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/ImportedModules/Module/ImportedFunctions/string" title="Process Section Imported Function" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/ImportedModules/Module/Name" title="Process Section Imported Module" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/PEChecksum/PEComputedAPI" title="Process SectionList MemorySection PEInfo PEChecksum PEComputedAPI" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/PEChecksum/PEFileAPI" title="Process SectionList MemorySection PEInfo PEChecksum PEFileAPI" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/PEChecksum/PEFileRaw" title="Process SectionList MemorySection PEInfo PEChecksum PEFileRaw" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/PETimeStamp" title="Process SectionList MemorySection PEInfo PETimeStamp" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/Sections/Section/DetectedCharacteristics" title="Process SectionList MemorySection PEInfo Sections Section Detected Characteristics" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/Sections/Section/DetectedSignatureKeys/string" title="Process SectionList MemorySection PEInfo Sections Section Detected Signature Keys" />
  <iocterm data-type="xs:string" display-type="float" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/Sections/Section/Entropy/CurveData/float" title="Process SectionList MemorySection PEInfo Sections Section Entropy Curve Data float" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/Sections/Section/Name" title="Process SectionList MemorySection PEInfo Sections Section Name" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/Sections/Section/SizeInBytes" title="Process SectionList MemorySection PEInfo Sections Section Size" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/Sections/Section/Type" title="Process SectionList MemorySection PEInfo Sections Section Type" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/Subsystem" title="Process SectionList MemorySection PEInfo Subsystem" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/Type" title="Process SectionList MemorySection PEInfo Type" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/PEInfo/Exports/DllName" title="Process Section Dll Export Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/Protection" title="Process Protection" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/RawFlags" title="Process Raw Flags" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/RegionSize" title="Process Region Size" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/RegionStart" title="Process Region Start" />
  <iocterm data-type="xs:string" display-type="sha1" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/Sha1sum" title="Process Section Sha1sum" />
  <iocterm data-type="xs:string" display-type="sha256" term-source="application/vnd.mandiant.mir" text="ProcessItem/SectionList/MemorySection/Sha256sum" title="Process Section Sha256sum" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SecurityID" title="Process Security ID" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/SecurityType" title="Process Security Type" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/StringList/string" title="Process String" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/Username" title="Process Username" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/arguments" title="Process Arguments" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/detectedAnomaly" title="Detected Anomaly" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/hidden" title="Process Hidden" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/kernelTime" title="Process Kernel Time" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/name" title="Process Name" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="ProcessItem/parentpid" title="Process Parent PID" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/path" title="Process Path" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="ProcessItem/pid" title="Process PID" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="ProcessItem/startTime" title="Process Start Time" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ProcessItem/userTime" title="Process User Time" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="RegistryItem/Hive" title="Registry Hive" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="RegistryItem/KeyPath" title="Registry Key Path" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="RegistryItem/Modified" title="Registry Key Modified Date" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="RegistryItem/NumSubKeys" title="Registry NumSubKeys" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="RegistryItem/NumValues" title="Registry NumValues" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="RegistryItem/Path" title="Registry Path" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="RegistryItem/ReportedLengthInBytes" title="Registry Reported Length In Bytes" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="RegistryItem/Text" title="Registry Text" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="RegistryItem/Type" title="Registry Type" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="RegistryItem/Username" title="Registry Username" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="RegistryItem/Value" title="Registry Value" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="RegistryItem/ValueName" title="Registry Value Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="RegistryItem/detectedAnomaly" title="Detected Anomaly" />
  <iocterm data-type="xs:string" display-type="IP" term-source="application/vnd.mandiant.mir" text="RouteEntryItem/Destination" title="Route Destination" />
  <iocterm data-type="xs:string" display-type="IP" term-source="application/vnd.mandiant.mir" text="RouteEntryItem/Gateway" title="Route Gateway" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="RouteEntryItem/Interface" title="Route Interface" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="RouteEntryItem/IsIPv6" title="Route Is IPv6" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="RouteEntryItem/Metric" title="Route Metric" />
  <iocterm data-type="xs:string" display-type="IP" term-source="application/vnd.mandiant.mir" text="RouteEntryItem/Netmask" title="Route Netmask" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="RouteEntryItem/Protocol" title="Route Protocol" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="RouteEntryItem/RouteAge" title="Route Age" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="RouteEntryItem/RouteType" title="Route Type" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ServiceItem/arguments" title="Service arguments" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ServiceItem/description" title="Service Description" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ServiceItem/descriptiveName" title="Service Descriptive Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ServiceItem/mode" title="Service mode" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ServiceItem/name" title="Service Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ServiceItem/path" title="Service Path" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ServiceItem/pathCertificateIssuer" title="Service Path Certificate Issuer" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ServiceItem/pathCertificateSubject" title="Service Path Certificate Subject" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ServiceItem/pathSignatureDescription" title="Service Path Signature Description" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="ServiceItem/pathSignatureExists" title="Service Path Signature Exists" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="ServiceItem/pathSignatureVerified" title="Service Path Signature Verified" />
  <iocterm data-type="xs:string" display-type="md5" term-source="application/vnd.mandiant.mir" text="ServiceItem/pathmd5sum" title="Service Path MD5" />
  <iocterm data-type="xs:string" display-type="sha1" term-source="application/vnd.mandiant.mir" text="ServiceItem/pathsha1sum" title="Service Path Sha1sum" />
  <iocterm data-type="xs:string" display-type="sha256" term-source="application/vnd.mandiant.mir" text="ServiceItem/pathsha256sum" title="Service Path Sha256sum" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="ServiceItem/pid" title="Service PID" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ServiceItem/serviceDLL" title="Service DLL" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ServiceItem/serviceDLLCertificateIssuer" title="Service DLL Certificate Issuer" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ServiceItem/serviceDLLCertificateSubject" title="Service DLL Certificate Subject" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ServiceItem/serviceDLLSignatureDescription" title="Service DLL Signature Description" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="ServiceItem/serviceDLLSignatureExists" title="Service DLLSignature Exists" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="ServiceItem/serviceDLLSignatureVerified" title="Service DLL Signature Verified" />
  <iocterm data-type="xs:string" display-type="md5" term-source="application/vnd.mandiant.mir" text="ServiceItem/serviceDLLmd5sum" title="Service DLL MD5" />
  <iocterm data-type="xs:string" display-type="sha1" term-source="application/vnd.mandiant.mir" text="ServiceItem/serviceDLLsha1sum" title="Service DLL Sha1sum" />
  <iocterm data-type="xs:string" display-type="sha256" term-source="application/vnd.mandiant.mir" text="ServiceItem/serviceDLLsha256sum" title="Service DLL Sha256sum" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ServiceItem/startedAs" title="Service Started As" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ServiceItem/status" title="Service Status" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="ServiceItem/type" title="Service Type" />
  <iocterm data-type="xs:string" display-type="string" text="Snort/Snort" title="Snort Signature" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/MAC" title="SystemInfo MAC" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/OS" title="SystemInfo Operating System" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/availphysical" title="SystemInfo Available Physical Memory" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/biosInfo/biosDate" title="SystemInfo BIOS Date" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/biosInfo/biosVersion" title="SystemInfo BIOS Version" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/buildNumber" title="SystemInfo Build Number" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/date" title="SystemInfo Date" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/directory" title="SystemInfo Directory" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/domain" title="SystemInfo Domain" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/hostname" title="SystemInfo Hostname" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/installDate" title="SystemInfo Install Date" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/machine" title="SystemInfo Machine" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/networkArray/networkInfo/MAC" title="SystemInfo networkArray networkInfo MAC" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/networkArray/networkInfo/adapter" title="SystemInfo Network Adapter" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/networkArray/networkInfo/description" title="SystemInfo Network Description" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/networkArray/networkInfo/dhcpLeaseExpires" title="SystemInfo Network DHCP Leas eExpires" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/networkArray/networkInfo/dhcpLeaseObtained" title="SystemInfo Network DHCP Lease Obtained" />
  <iocterm data-type="xs:string" display-type="IP" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/networkArray/networkInfo/dhcpServerArray/dhcpServer" title="SystemInfo Network DHCP Server" />
  <iocterm data-type="xs:string" display-type="IP" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/networkArray/networkInfo/ipArray/ipInfo/ipAddress" title="SystemInfo Network IP Address" />
  <iocterm data-type="xs:string" display-type="IP" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/networkArray/networkInfo/ipArray/ipInfo/subnetMask" title="SystemInfo Network Subnet Mask" />
  <iocterm data-type="xs:string" display-type="IP" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/networkArray/networkInfo/ipGatewayArray/ipGateway" title="SystemInfo Network IP Gateway" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/patchLevel" title="SystemInfo Patch Level" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/procType" title="SystemInfo Proc Type" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/processor" title="SystemInfo Processor" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/productID" title="SystemInfo Product ID" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/productName" title="SystemInfo Product Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/regOrg" title="SystemInfo Registered Org" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/regOwner" title="SystemInfo Registered Owner" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/timezoneDST" title="SystemInfo Timezone DST" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/timezoneStandard" title="SystemInfo Timezone Standard" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/totalphysical" title="SystemInfo Total Physical" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/uptime" title="SystemInfo Iptime" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemInfoItem/user" title="SystemInfo User" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemRestoreItem/RestorePointName" title="SystemRestore Restore Point Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemRestoreItem/RestorePointFullPath" title="SystemRestore Full Path" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemRestoreItem/RestorePointDescription" title="SystemRestore Description" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemRestoreItem/RestorePointType" title="SystemRestore Type" />
  <iocterm data-type="xs:string" display-type="date" term-source="application/vnd.mandiant.mir" text="SystemRestoreItem/Created" title="SystemRestore Created" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemRestoreItem/RegistryHives/String" title="SystemRestore Registry Hives" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemRestoreItem/ChangeLogFileName" title="SystemRestore ChangeLog Filename" />
  <iocterm data-type="xs:string" display-type="int" term-source="application/vnd.mandiant.mir" text="SystemRestoreItem/ChangeLogEntrySequenceNumber" title="SystemRestore ChangeLog Seq. Number" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemRestoreItem/ChangeLogEntryType" title="SystemRestore ChangeLog Entry Type" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemRestoreItem/ChangeLogEntryFlags" title="SystemRestore ChangeLog Entry  Flags" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemRestoreItem/FileAttributes" title="SystemRestore File Attributes" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemRestoreItem/OriginalFileName" title="SystemRestore Original Filename" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemRestoreItem/BackupFileName" title="SystemRestore Backup Filename" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemRestoreItem/AclChangeUsername" title="SystemRestore Acl Change Username" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemRestoreItem/AclChangeSecurityID" title="SystemRestore Acl Change Security ID" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="SystemRestoreItem/OriginalShortFileName" title="SystemRestore Original Short FileName" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/AccountLogonType" title="Task Account Logon Type" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/AccountName" title="Task Account Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/AccountRunLevel" title="Task Account Run Level" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/ActionList/Action/ActionType" title="Task Action Type" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/ActionList/Action/COMClassId" title="Task Action COM Class Id" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/ActionList/Action/COMData" title="Task Action COM Data" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/ActionList/Action/DigitalSignature/CertificateIssuer" title="Task Action Digital Signature Certificate Issuer" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/ActionList/Action/DigitalSignature/CertificateSubject" title="Task Action Digital Signature Certificate Subject" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/ActionList/Action/DigitalSignature/Description" title="Task Action Digital Signature Description" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="TaskItem/ActionList/Action/DigitalSignature/SignatureExists" title="Task Action Digital Signature Signature Exists" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="TaskItem/ActionList/Action/DigitalSignature/SignatureVerified" title="Task Action Digital Signature Signature Verified" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/ActionList/Action/EmailAttachments" title="Task Action Email Attachments" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/ActionList/Action/EmailBCC" title="Task Action Email BCC" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/ActionList/Action/EmailBody" title="Task Action Email Body" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/ActionList/Action/EmailCC" title="Task Action Email CC" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/ActionList/Action/EmailFrom" title="Task Action Email From" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/ActionList/Action/EmailReplyTo" title="Task Action Email ReplyTo" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/ActionList/Action/EmailServer" title="Task Action Email Server" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/ActionList/Action/EmailSubject" title="Task Action Email Subject" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/ActionList/Action/EmailTo" title="Task Action Email To" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/ActionList/Action/ExecArguments" title="Task Action Exec Arguments" />
  <iocterm data-type="xs:string" display-type="md5" term-source="application/vnd.mandiant.mir" text="TaskItem/ActionList/Action/ExecProgramMd5sum" title="Task Action Exec Program MD5" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/ActionList/Action/ExecProgramPath" title="Task Action Exec Program Path" />
  <iocterm data-type="xs:string" display-type="sha1" term-source="application/vnd.mandiant.mir" text="TaskItem/ActionList/Action/ExecProgramSha1sum" title="Task Action Exec Program Sha1sum" />
  <iocterm data-type="xs:string" display-type="sha256" term-source="application/vnd.mandiant.mir" text="TaskItem/ActionList/Action/ExecProgramSha256sum" title="Task Action Exec Program Sha256sum" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/ActionList/Action/ExecWorkingDirectory" title="Task Action Exec Working Directory" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/ActionList/Action/ShowMessageBody" title="Task Action Show Message Body" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/ActionList/Action/ShowMessageTitle" title="Task Action Show Message Title" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/ApplicationName" title="Task Application Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/CertificateIssuer" title="Task Certificate Issuer" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/CertificateSubject" title="Task Certificate Subject" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/Comment" title="Task Comment" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="TaskItem/CreationDate" title="Task Creation Date" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/Creator" title="Task Creator" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/ExitCode" title="Task Exit Code" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/Flag" title="Task Flag" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/MaxRunTime" title="Task Max Run Time" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="TaskItem/MostRecentRunTime" title="Task Most Recent Run Time" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/Name" title="Task Name" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="TaskItem/NextRunTime" title="Task Next Run Time" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/Parameters" title="Task Parameters" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/Priority" title="Task Priority" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/SignatureDescription" title="Task Signature Description" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/SignatureExists" title="Task Signature Exists" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="TaskItem/SignatureVerified" title="Task Signature Verified" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/Status" title="Task Status" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="TaskItem/TriggerList/Trigger/TriggerBegin" title="Task Trigger Begin" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/TriggerList/Trigger/TriggerDelay" title="Task Trigger Delay" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="TaskItem/TriggerList/Trigger/TriggerEnabled" title="Task Trigger Enabled" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/TriggerList/Trigger/TriggerEnd" title="Task Trigger End" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/TriggerList/Trigger/TriggerFrequency" title="Task Trigger Frequency" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/TriggerList/Trigger/TriggerMaxRunTime" title="Task Trigger Max Run Time" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/TriggerList/Trigger/TriggerSessionChangeType" title="Task Trigger Session Change Type" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/TriggerList/Trigger/TriggerSubscription" title="Task Trigger Subscription" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/TriggerList/Trigger/TriggerUsername" title="Task Trigger Username" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/TriggerList/Trigger/TriggerValueQueries" title="Task Trigger Value Queries" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/VirtualPath" title="Task Virtual Path" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/WorkItemData" title="Task Work Data" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="TaskItem/WorkingDirectory" title="Task Working Directory" />
  <iocterm data-type="xs:string" display-type="md5" term-source="application/vnd.mandiant.mir" text="TaskItem/md5sum" title="Task MD5" />
  <iocterm data-type="xs:string" display-type="sha1" term-source="application/vnd.mandiant.mir" text="TaskItem/sha1sum" title="Task Sha1sum" />
  <iocterm data-type="xs:string" display-type="sha256" term-source="application/vnd.mandiant.mir" text="TaskItem/sha256sum" title="Task Sha256sum" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="UrlHistoryItem/BrowserName" title="UrlHistory Browser Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="UrlHistoryItem/BrowserVersion" title="UrlHistory Browser Version" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="UrlHistoryItem/FirstBookmarkDate" title="UrlHistory First Bookmark Date" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="UrlHistoryItem/FirstVisitDate" title="UrlHistory First Visit Date" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="UrlHistoryItem/Hidden" title="UrlHistory Hidden" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="UrlHistoryItem/HostName" title="UrlHistory Host Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="UrlHistoryItem/IndexedContent" title="UrlHistory Indexed Content" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="UrlHistoryItem/LastVisitDate" title="UrlHistory Last Visit Date" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="UrlHistoryItem/LastVisitDateLocal" title="UrlHistory Last Visit Date Local" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="UrlHistoryItem/PageTitle" title="UrlHistory Page Title" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="UrlHistoryItem/Profile" title="UrlHistory Profile" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="UrlHistoryItem/Thumbnail" title="UrlHistory Thumbnail" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="UrlHistoryItem/Typed" title="UrlHistory Typed" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="UrlHistoryItem/URL" title="UrlHistory URL" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="UrlHistoryItem/Username" title="UrlHistory Username" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="UrlHistoryItem/VisitCount" title="UrlHistory Visit Count" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="UrlHistoryItem/VisitFrom" title="UrlHistory Visit From" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="UrlHistoryItem/VisitType" title="UrlHistory Visit Type" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="UserItem/LastLogin" title="User Last Login" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="UserItem/SecurityID" title="User Security ID" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="UserItem/SecurityType" title="User Security Type" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="UserItem/Username" title="User Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="UserItem/description" title="User Description" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="UserItem/disabled" title="User Disabled" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="UserItem/fullname" title="User Fullname" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="UserItem/grouplist/groupname" title="User Group Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="UserItem/homedirectory" title="User Home Directory" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="UserItem/lockedout" title="User Lockedout" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="UserItem/passwordrequired" title="User Password Required" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="UserItem/scriptpath" title="User Script Path" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="UserItem/userpasswordage" title="User Password Age" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="VolumeItem/ActualAvailableAllocationUnits" title="Volume Actual Available Allocation Units" />
  <iocterm data-type="xs:int" display-type="int" term-source="application/vnd.mandiant.mir" text="VolumeItem/BytesPerSector" title="Volume Byte sPer Sector" />
  <iocterm data-type="xs:dateTime" display-type="date" term-source="application/vnd.mandiant.mir" text="VolumeItem/CreationTime" title="Volume Creation Time" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="VolumeItem/DevicePath" title="Volume Device Path" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="VolumeItem/DriveLetter" title="Volume Drive Letter" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="VolumeItem/FileSystemFlags" title="Volume File System Flags" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="VolumeItem/FileSystemName" title="Volume File System Name" />
  <iocterm data-type="xs:string" display-type="bool" term-source="application/vnd.mandiant.mir" text="VolumeItem/IsMounted" title="Volume Is Mounted" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="VolumeItem/Name" title="Volume Name" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="VolumeItem/SectorsPerAllocationUnit" title="Volume Sectors Per Allocation Unit" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="VolumeItem/SerialNumber" title="Volume Serial Number" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="VolumeItem/TotalAllocationUnits" title="Volume Total Allocation Units" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="VolumeItem/Type" title="Volume Type" />
  <iocterm data-type="xs:string" display-type="string" term-source="application/vnd.mandiant.mir" text="VolumeItem/VolumeName" title="Volume Name" />
  <iocterm data-type="xs:string" display-type="string" text="Yara/Yara" title="Yara Rule" />
</ioctermlist>
"""