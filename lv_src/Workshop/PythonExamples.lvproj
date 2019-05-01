<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="18008000">
	<Property Name="NI.LV.All.SourceOnly" Type="Bool">true</Property>
	<Item Name="My Computer" Type="My Computer">
		<Property Name="NI.SortType" Type="Int">3</Property>
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="py_src" Type="Folder">
			<Item Name="ImageClassification.py" Type="Document" URL="../../../py_src/ImageClassification.py"/>
			<Item Name="PythonNodeExamples.py" Type="Document" URL="../../../py_src/PythonNodeExamples.py"/>
		</Item>
		<Item Name="utilities" Type="Folder">
			<Item Name="GetPathToModule.vi" Type="VI" URL="../GetPathToModule.vi"/>
		</Item>
		<Item Name="HelloWorld.vi" Type="VI" URL="../HelloWorld.vi"/>
		<Item Name="Add.vi" Type="VI" URL="../Add.vi"/>
		<Item Name="MaxAndMin.vi" Type="VI" URL="../MaxAndMin.vi"/>
		<Item Name="CalculateDaysSince.vi" Type="VI" URL="../CalculateDaysSince.vi"/>
		<Item Name="GetValueForKey.vi" Type="VI" URL="../GetValueForKey.vi"/>
		<Item Name="FindFaces.vi" Type="VI" URL="../FindFaces.vi"/>
		<Item Name="FindCorners.vi" Type="VI" URL="../FindCorners.vi"/>
		<Item Name="Dependencies" Type="Dependencies"/>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
