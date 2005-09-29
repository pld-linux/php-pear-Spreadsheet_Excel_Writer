%include	/usr/lib/rpm/macros.php
%define		_class		Spreadsheet
%define		_subclass	Excel
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}_Writer

Summary:	%{_pearname} - package for generating Excel spreadsheets
Summary(pl):	%{_pearname} - pakiet generuj�cy arkusze Excela
Name:		php-pear-%{_pearname}
Version:	0.8
Release:	2.1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	4a5354e3fbd5deb2d826bcbcd4e7295d
URL:		http://pear.php.net/package/Spreadsheet_Excel_Writer/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spreadsheet_Excel_Writer was born as a porting of the
Spreadsheet::WriteExcel Perl module to PHP. It allows writing of Excel
spreadsheets without the need for COM objects. It supports formulas,
images (BMP) and all kinds of formatting for text and cells. It
currently supports the BIFF5 format (Excel 5.0), so functionality
appeared in the latest Excel versions is not yet available.

In PEAR status of this package is: %{_status}.

%description -l pl
Spreadsheet_Excel_Writer narodzi� si� jako port do PHP perlowego
modu�u Spreadsheet::WriteExcel. Pozwala na zapisywanie arkuszy Excela
bez potrzeby u�ywania obiekt�w COM. Ma wsparcie dla formularzy,
rysunk�w (BMP) oraz wszelkiego typu formatowania tekstu oraz kom�rek.
Aktualnie wspiera format BIFF5 (Excel 5.0), wi�c funkcjonalno��
ostatnich wersji Excela nie jest jeszcze dost�pna.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%dir %{php_pear_dir}/%{_class}/
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Writer
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Writer/*.php
