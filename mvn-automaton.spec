#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-automaton
Version  : 1.11.8
Release  : 3
URL      : https://repo1.maven.org/maven2/dk/brics/automaton/automaton/1.11-8/automaton-1.11-8.jar
Source0  : https://repo1.maven.org/maven2/dk/brics/automaton/automaton/1.11-8/automaton-1.11-8.jar
Source1  : https://repo1.maven.org/maven2/dk/brics/automaton/automaton/1.11-8/automaton-1.11-8.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: mvn-automaton-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-automaton package.
Group: Data

%description data
data components for the mvn-automaton package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/dk/brics/automaton/automaton/1.11-8
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/dk/brics/automaton/automaton/1.11-8/automaton-1.11-8.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/dk/brics/automaton/automaton/1.11-8
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/dk/brics/automaton/automaton/1.11-8/automaton-1.11-8.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/dk/brics/automaton/automaton/1.11-8/automaton-1.11-8.jar
/usr/share/java/.m2/repository/dk/brics/automaton/automaton/1.11-8/automaton-1.11-8.pom
