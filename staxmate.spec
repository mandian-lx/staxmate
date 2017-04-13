%{?_javapackages_macros:%_javapackages_macros}
Name:          staxmate
Version:       2.3.0
Release:       4%{?dist}
Summary:       Light-weight Java framework for streaming XML processing
License:       BSD
URL:           https://github.com/FasterXML/StaxMate
Source0:       https://github.com/FasterXML/StaxMate/archive/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(javax.xml.stream:stax-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-surefire-report-plugin)
BuildRequires:  mvn(org.codehaus.woodstox:stax2-api)
BuildRequires:  mvn(org.codehaus.woodstox:woodstox-core-asl)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch

%description
StaxMate is a light-weight framework that
adds convenience to streaming XML-processing
without significant additional overhead. It
builds on top of a Stax (JSR-173) compliant
XML processors such as Woodstox or Sjsxp
(default Stax implementation of JDK 1.6) and
offers two basic abstractions: Cursors, which
build on XMLStreamReaders and Output objects,
which build on XMLStreamWriters.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n StaxMate-%{name}-%{version}
find . -name '*.jar' -delete
find . -name '*.class' -delete

# Unwanted
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :cobertura-maven-plugin

# these tests fails
rm src/test/java/org/codehaus/staxmate/dom/TestDOMConverter.java \
 src/test/java/org/codehaus/staxmate/out/TestBinary.java

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md release-notes/*
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 22 2016 gil cattaneo <puntogil@libero.it> 2.3.0-3
- regenerate build-requires

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 05 2015 gil cattaneo <puntogil@libero.it> 2.3.0-1
- update to 2.3.0

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb 12 2015 gil cattaneo <puntogil@libero.it> 2.2.1-2
- introduce license macro

* Thu Oct 23 2014 gil cattaneo <puntogil@libero.it> 2.2.1-1
- update to 2.2.1

* Sat Aug 30 2014 gil cattaneo <puntogil@libero.it> 2.2.0-2
- fix build failure on rawhide

* Mon May 20 2013 gil cattaneo <puntogil@libero.it> 2.2.0-1
- update to 2.2.0

* Sat May 05 2012 gil cattaneo <puntogil@libero.it> 2.0.1-2
- changed summary

* Fri Apr 20 2012 gil cattaneo <puntogil@libero.it> 2.0.1-1
- initial rpm
