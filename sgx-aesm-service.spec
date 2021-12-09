%define _aesm_service_path /opt/intel/sgx-aesm-service
%define _ra_service_path /opt/intel/sgx-ra-service
%define _dcap_pccs_path /opt/intel/sgx-dcap-pccs
%define _psw_version 2.15.100.0
%define _dcap_version 1.12.100.0
%define _license_file COPYING

Name:           sgx-aesm-service
Version:        %{_psw_version}
Release:        1%{?dist}
Summary:        Intel(R) Software Guard Extensions AESM Service

License:        BSD
URL:            https://github.com/intel/linux-sgx
Source0:        https://download.01.org/intel-sgx/rpm_onespec/psw-dcap-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  binutils
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  redhat-rpm-config
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  libcurl-devel
BuildRequires:  python
BuildRequires:  perl

# SGX is a feature supported and verified on x86_64 only.
ExclusiveArch:	x86_64

%description
Intel(R) Software Guard Extensions AESM Service

%package -n libsgx-ae-epid
Version:       %{_psw_version}
Summary:       Intel(R) Software Guard Extensions QE and PvE

%description -n libsgx-ae-epid
Intel(R) Software Guard Extensions QE and PvE

%package -n libsgx-ae-le
Version:       %{_psw_version}
Summary:       Intel(R) Software Guard Extensions LE

%description -n libsgx-ae-le
Intel(R) Software Guard Extensions LE

%package -n libsgx-ae-pce
Version:       %{_psw_version}
Summary:       Intel(R) Software Guard Extensions PCE

%description -n libsgx-ae-pce
Intel(R) Software Guard Extensions PCE

%package -n libsgx-aesm-ecdsa-plugin
Version:       %{_psw_version}
Summary:       ECDSA Quote Plugin for Intel(R) Software Guard Extensions AESM Service
Requires:      %{name} >= %{version}-%{release} libsgx-qe3-logic >= %{_dcap_version}-%{release} libsgx-aesm-pce-plugin >= %{version}-%{release}

%description -n libsgx-aesm-ecdsa-plugin
ECDSA Quote Plugin for Intel(R) Software Guard Extensions AESM Service

%package -n libsgx-aesm-epid-plugin
Version:       %{_psw_version}
Summary:       EPID Quote Plugin for Intel(R) Software Guard Extensions AESM Service
Requires:      %{name} >= %{version}-%{release} libsgx-ae-epid >= %{version}-%{release} libsgx-aesm-pce-plugin >= %{version}-%{release}

%description -n libsgx-aesm-epid-plugin
EPID Quote Plugin for Intel(R) Software Guard Extensions AESM Service

%package -n libsgx-aesm-launch-plugin
Version:       %{_psw_version}
Summary:       Launch Plugin for Intel(R) Software Guard Extensions AESM Service
Requires:      %{name} >= %{version}-%{release} libsgx-ae-le >= %{version}-%{release}

%description -n libsgx-aesm-launch-plugin
Launch Plugin for Intel(R) Software Guard Extensions AESM Service

%package -n libsgx-aesm-pce-plugin
Version:       %{_psw_version}
Summary:       PCE Plugin for Intel(R) Software Guard Extensions AESM Service
Requires:      %{name} >= %{version}-%{release} libsgx-pce-logic >= %{_dcap_version}-%{release}

%description -n libsgx-aesm-pce-plugin
PCE Plugin for Intel(R) Software Guard Extensions AESM Service

%package -n libsgx-aesm-quote-ex-plugin
Version:       %{_psw_version}
Summary:       Unified Quote Plugin for Intel(R) Software Guard Extensions AESM Service
Requires:      %{name} >= %{version}-%{release} libsgx-aesm-ecdsa-plugin >= %{version}-%{release}
Recommends:    libsgx-aesm-epid-plugin >= %{version}-%{release}

%description -n libsgx-aesm-quote-ex-plugin
Unified Quote Plugin for Intel(R) Software Guard Extensions AESM Service

%package -n libsgx-epid
Version:       %{_psw_version}
Summary:       Intel(R) Software Guard Extensions EPID Quote Service
Recommends:    libsgx-aesm-epid-plugin >= %{version}-%{release}

%description -n libsgx-epid
Intel(R) Software Guard Extensions EPID Quote Service

%package -n libsgx-epid-devel
Version:       %{_psw_version}
Summary:       Intel(R) Software Guard Extensions EPID Quote Service for Developers
Requires:      libsgx-epid = %{version}-%{release} libsgx-headers >= %{version}-%{release}

%description -n libsgx-epid-devel
Intel(R) Software Guard Extensions EPID Quote Service for Developers

%package -n libsgx-launch
Version:       %{_psw_version}
Summary:       Intel(R) Software Guard Extensions Launch Service
Recommends:    libsgx-aesm-launch-plugin >= %{version}-%{release}

%description -n libsgx-launch
Intel(R) Software Guard Extensions Launch Service

%package -n libsgx-launch-devel
Version:       %{_psw_version}
Summary:       Intel(R) Software Guard Extensions Launch Service for Developers
Requires:      libsgx-launch = %{version}-%{release} libsgx-headers >= %{version}-%{release}

%description -n libsgx-launch-devel
Intel(R) Software Guard Extensions Launch Service for Developers

%package -n libsgx-quote-ex
Version:       %{_psw_version}
Summary:       Intel(R) Software Guard Extensions Unified Quote Service
Recommends:    libsgx-aesm-quote-ex-plugin >= %{version}-%{release}

%description -n libsgx-quote-ex
Intel(R) Software Guard Extensions Unified Quote Service

%package -n libsgx-quote-ex-devel
Version:       %{_psw_version}
Summary:       Intel(R) Software Guard Extensions Unified Quote Service for Developers
Requires:      libsgx-quote-ex = %{version}-%{release} libsgx-headers >= %{version}-%{release}

%description -n libsgx-quote-ex-devel 
Intel(R) Software Guard Extensions Unified Quote Service for Developers

%package -n libsgx-headers
Version:       %{_psw_version}
Summary:       Intel(R) Software Guard Extensions Basic Headers

%description -n libsgx-headers
Intel(R) Software Guard Extensions Basic Headers

%package -n libsgx-urts
Version:       %{_psw_version}
Summary:       Intel(R) Software Guard Extensions uRTS
Requires:      libsgx-enclave-common >= %{version}-%{release}

%description -n libsgx-urts
Intel(R) Software Guard Extensions uRTS

%package -n libsgx-uae-service
Version:       %{_psw_version}
Summary:       Intel(R) Software Guard Extensions Untrusted AE Service
Requires:      libsgx-epid >= %{version}-%{release} libsgx-launch >= %{version}-%{release} libsgx-quote-ex >= %{version}-%{release}

%description -n libsgx-uae-service
Intel(R) Software Guard Extensions Untrusted AE Service

%package -n libsgx-enclave-common
Version:       %{_psw_version}
Summary:       Intel(R) Software Guard Extensions Enclave Common Loader
Recommends:    libsgx-launch >= %{version}-%{release}

%description -n libsgx-enclave-common
Intel(R) Software Guard Extensions Enclave Common Loader

%package -n libsgx-enclave-common-devel
Version:       %{_psw_version}
Summary:       Intel(R) Software Guard Extensions Enclave Common Loader for Developers
Requires:      libsgx-enclave-common = %{version}-%{release} libsgx-headers >= %{version}-%{release}

%description -n libsgx-enclave-common-devel
Intel(R) Software Guard Extensions Enclave Common Loader for Developers

%package -n libsgx-ae-qe3
Version:       %{_dcap_version}
Summary:       Intel(R) Software Guard Extensions QE3

%description -n libsgx-ae-qe3
Intel(R) Software Guard Extensions QE3

%package -n libsgx-ae-qve
Version:       %{_dcap_version}
Summary:       Intel(R) Software Guard Extensions QVE

%description -n libsgx-ae-qve
Intel(R) Software Guard Extensions QVE

%package -n libsgx-qe3-logic
Version:       %{_dcap_version}
Summary:       Intel(R) Software Guard Extensions QE3 logic
Requires:      libsgx-urts >= %{_psw_version}-%{release} libsgx-ae-qe3 >= %{version}-%{release}

%description -n libsgx-qe3-logic
Intel(R) Software Guard Extensions QE3 logic

%package -n libsgx-pce-logic
Version:       %{_dcap_version}
Summary:       Intel(R) Software Guard Extensions PCE logic
Requires:      libsgx-urts >= %{_psw_version}-%{release} libsgx-ae-pce >= %{_psw_version}-%{release}

%description -n libsgx-pce-logic
Intel(R) Software Guard Extensions PCE logic

%package -n libsgx-dcap-default-qpl
Version:       %{_dcap_version}
Summary:       Intel(R) Software Guard Extensions Default Quote Provider Library

%description -n libsgx-dcap-default-qpl
Intel(R) Software Guard Extensions Default Quote Provider Library

%package -n libsgx-dcap-default-qpl-devel
Version:       %{_dcap_version}
Summary:       Intel(R) Software Guard Extensions Default Quote Provider Library for Developers
Requires:      libsgx-dcap-default-qpl = %{version}-%{release}

%description -n libsgx-dcap-default-qpl-devel
Intel(R) Software Guard Extensions Default Quote Provider Library for Developers

%package -n libsgx-dcap-ql
Version:       %{_dcap_version}
Summary:       Intel(R) Software Guard Extensions Data Center Attestation Primitives Quote Generation Library
Requires:      libsgx-qe3-logic >= %{version}-%{release} libsgx-pce-logic >= %{version}-%{release} libsgx-ae-qve >= %{version}-%{release}
Recommends:    libsgx-dcap-quote-verify >= %{version}-%{release} libsgx-quote-ex >= %{_psw_version}-%{release}

%description -n libsgx-dcap-ql
Intel(R) Software Guard Extensions Data Center Attestation Primitives Quote Generation Library

%package -n libsgx-dcap-ql-devel
Version:       %{_dcap_version}
Summary:       Intel(R) Software Guard Extensions Data Center Attestation Primitives Quote Generation Library for Developers
Requires:      libsgx-dcap-ql = %{version}-%{release} libsgx-headers >= %{_psw_version}-%{release}

%description -n libsgx-dcap-ql-devel
Intel(R) Software Guard Extensions Data Center Attestation Primitives Quote Generation Library for Developers

%package -n libsgx-dcap-quote-verify
Version:       %{_dcap_version}
Summary:       Intel(R) Software Guard Extensions Data Center Attestation Primitives Quote Verification Library
Recommends:    libsgx-ae-qve >= %{version}-%{release} libsgx-urts >= %{_psw_version}-%{release}

%description -n libsgx-dcap-quote-verify
Intel(R) Software Guard Extensions Data Center Attestation Primitives Quote Verification Library

%package -n libsgx-dcap-quote-verify-devel
Version:       %{_dcap_version}
Summary:       Intel(R) Software Guard Extensions Data Center Attestation Primitives Quote Verification Library for Developers
Requires:      libsgx-dcap-quote-verify = %{version}-%{release} libsgx-headers >= %{_psw_version}-%{release}

%description -n libsgx-dcap-quote-verify-devel
Intel(R) Software Guard Extensions Data Center Attestation Primitives Quote Verification Library for Developers

%package -n sgx-dcap-pccs
Version:       %{_dcap_version}
Summary:       Intel(R) Software Guard Extensions PCK Caching Service
Requires:      gcc gcc-c++ make

%description -n sgx-dcap-pccs
Intel(R) Software Guard Extensions PCK Caching Service

%package -n libsgx-ra-network
Version:       %{_dcap_version}
Summary:       Intel(R) Software Guard Extensions Registration Agent Network Library

%description -n libsgx-ra-network
Intel(R) Software Guard Extensions Registration Agent Network Library

%package -n libsgx-ra-network-devel
Version:       %{_dcap_version}
Summary:       Intel(R) Software Guard Extensions Registration Agent Network Library for Developers
Requires:      libsgx-ra-network = %{version}-%{release}

%description -n libsgx-ra-network-devel
Intel(R) Software Guard Extensions Registration Agent Network Library for Developers

%package -n libsgx-ra-uefi
Version:       %{_dcap_version}
Summary:       Intel(R) Software Guard Extensions Registration Agent UEFI Library

%description -n libsgx-ra-uefi
Intel(R) Software Guard Extensions Registration Agent UEFI Library

%package -n libsgx-ra-uefi-devel
Version:       %{_dcap_version}
Summary:       Intel(R) Software Guard Extensions Registration Agent UEFI Library for Developers
Requires:      libsgx-ra-uefi = %{version}-%{release}

%description -n libsgx-ra-uefi-devel
Intel(R) Software Guard Extensions Registration Agent UEFI Library for Developers

%package -n sgx-ra-service
Version:       %{_dcap_version}
Summary:       Intel(R) Software Guard Extensions Registration Agent Service
Requires:      libsgx-ra-uefi >= %{version}-%{release} libsgx-ra-network >= %{version}-%{release}

%description -n sgx-ra-service
Intel(R) Software Guard Extensions Registration Agent Service

%package -n sgx-pck-id-retrieval-tool
Version:       %{_dcap_version}
Summary:       Intel(R) Software Guard Extensions PCK Certs Retrieve Tool
Recommends:    libsgx-urts >= %{_psw_version} libsgx-dcap-ql >= %{version}-%{release} libsgx-ra-uefi >= %{version}-%{release}

%description -n sgx-pck-id-retrieval-tool
Intel(R) Software Guard Extensions:this tool is used to collect the platform information to retrieve the PCK certs from PCS(Provisioning Certification Server)

%prep
%setup -qc

%build
make %{?_smp_mflags} build

%install
make DESTDIR=%{?buildroot} install

for pkg in $(ls -A %{?buildroot} 2> /dev/null); do
    install -d %{?buildroot}/${pkg}/%{_docdir}/${pkg}
    find license -type f -print0 | \
    xargs -0 -n1 cat >> %{?buildroot}/${pkg}/%{_docdir}/${pkg}/%{_license_file}
    find %{?buildroot}/${pkg} -type d -links 2 | \
    sed -e "s#^%{?buildroot}/${pkg}##" | \
    grep -v "^%{_libdir}" | \
    grep -v "^%{_includedir}" | \
    grep -v "^%{_sysconfdir}" | \
    grep -v "^%{_usr}/local/bin" | \
    grep -v "^%{_aesm_service_path}" | \
    grep -v "^%{_dcap_pccs_path}" | \
    grep -v "^%{_ra_service_path}" | \
    sed -e "s#^#%dir #" > %{_specdir}/list-${pkg}
    for f in $(find %{?buildroot}/${pkg}); do
        if [ -d ${f} ]; then
            echo ${f} | sed -e "s#^%{?buildroot}/${pkg}##" | \
            grep -E "^%{_aesm_service_path}|^%{_dcap_pccs_path}|^%{_ra_service_path}" | \
            sed -e "s#^#%dir #" >> %{_specdir}/list-${pkg}
        else
            echo ${f} | \
            sed -e "s#^%{?buildroot}/${pkg}##" >> %{_specdir}/list-${pkg}
        fi
    done
    cp -r %{?buildroot}/${pkg}/* %{?buildroot}/
    rm -fr %{?buildroot}/${pkg}
    sed -i -e 's:^/etc/.*\.conf:%config &:' \
           -e 's:^%{_dcap_pccs_path}/config/default\.json:%config &:' %{_specdir}/list-${pkg}
done

%clean
make clean

%files -f %{_specdir}/list-%{name}
%files -n libsgx-ae-epid -f %{_specdir}/list-libsgx-ae-epid
%files -n libsgx-ae-le -f %{_specdir}/list-libsgx-ae-le
%files -n libsgx-ae-pce -f %{_specdir}/list-libsgx-ae-pce
%files -n libsgx-aesm-ecdsa-plugin -f %{_specdir}/list-libsgx-aesm-ecdsa-plugin
%files -n libsgx-aesm-epid-plugin -f %{_specdir}/list-libsgx-aesm-epid-plugin
%files -n libsgx-aesm-launch-plugin -f %{_specdir}/list-libsgx-aesm-launch-plugin
%files -n libsgx-aesm-pce-plugin -f %{_specdir}/list-libsgx-aesm-pce-plugin
%files -n libsgx-aesm-quote-ex-plugin -f %{_specdir}/list-libsgx-aesm-quote-ex-plugin
%files -n libsgx-epid -f %{_specdir}/list-libsgx-epid
%files -n libsgx-epid-devel -f %{_specdir}/list-libsgx-epid-devel
%files -n libsgx-launch -f %{_specdir}/list-libsgx-launch
%files -n libsgx-launch-devel -f %{_specdir}/list-libsgx-launch-devel
%files -n libsgx-quote-ex -f %{_specdir}/list-libsgx-quote-ex
%files -n libsgx-quote-ex-devel -f %{_specdir}/list-libsgx-quote-ex-devel
%files -n libsgx-headers -f %{_specdir}/list-libsgx-headers
%files -n libsgx-urts -f %{_specdir}/list-libsgx-urts
%files -n libsgx-uae-service -f %{_specdir}/list-libsgx-uae-service
%files -n libsgx-enclave-common -f %{_specdir}/list-libsgx-enclave-common
%files -n libsgx-enclave-common-devel -f %{_specdir}/list-libsgx-enclave-common-devel
%files -n libsgx-ae-qe3 -f %{_specdir}/list-libsgx-ae-qe3
%files -n libsgx-ae-qve -f %{_specdir}/list-libsgx-ae-qve
%files -n libsgx-qe3-logic -f %{_specdir}/list-libsgx-qe3-logic
%files -n libsgx-pce-logic -f %{_specdir}/list-libsgx-pce-logic
%files -n libsgx-dcap-default-qpl -f %{_specdir}/list-libsgx-dcap-default-qpl
%files -n libsgx-dcap-default-qpl-devel -f %{_specdir}/list-libsgx-dcap-default-qpl-devel
%files -n libsgx-dcap-ql -f %{_specdir}/list-libsgx-dcap-ql
%files -n libsgx-dcap-ql-devel -f %{_specdir}/list-libsgx-dcap-ql-devel
%files -n libsgx-dcap-quote-verify -f %{_specdir}/list-libsgx-dcap-quote-verify
%files -n libsgx-dcap-quote-verify-devel -f %{_specdir}/list-libsgx-dcap-quote-verify-devel
%files -n sgx-dcap-pccs -f %{_specdir}/list-sgx-dcap-pccs
%files -n libsgx-ra-network -f %{_specdir}/list-libsgx-ra-network
%files -n libsgx-ra-network-devel -f %{_specdir}/list-libsgx-ra-network-devel
%files -n libsgx-ra-uefi -f %{_specdir}/list-libsgx-ra-uefi
%files -n libsgx-ra-uefi-devel -f %{_specdir}/list-libsgx-ra-uefi-devel
%files -n sgx-ra-service -f %{_specdir}/list-sgx-ra-service
%files -n sgx-pck-id-retrieval-tool -f %{_specdir}/list-sgx-pck-id-retrieval-tool

%post
if [ -x %{_aesm_service_path}/startup.sh ]; then %{_aesm_service_path}/startup.sh; fi

%preun
if [ -x %{_aesm_service_path}/cleanup.sh ]; then %{_aesm_service_path}/cleanup.sh; fi

%post -n sgx-dcap-pccs
if [ -x %{_dcap_pccs_path}/startup.sh ]; then %{_dcap_pccs_path}/startup.sh; fi

%preun -n sgx-dcap-pccs
if [ -x %{_dcap_pccs_path}/cleanup.sh ]; then %{_dcap_pccs_path}/cleanup.sh; fi

%post -n sgx-ra-service
if [ -x %{_ra_service_path}/startup.sh ]; then %{_ra_service_path}/startup.sh; fi

%preun -n sgx-ra-service
if [ -x %{_ra_service_path}/cleanup.sh ]; then %{_ra_service_path}/cleanup.sh; fi

%post -n libsgx-enclave-common
trigger_udev() {
    if ! which udevadm &> /dev/null; then
        return 0
    fi
    udevadm control --reload || :
    udevadm trigger || :
}

trigger_udev

%post -n libsgx-ae-pce
trigger_udev() {
    if ! which udevadm &> /dev/null; then
        return 0
    fi
    udevadm control --reload || :
    udevadm trigger || :
}

# Add sgx_prv for in-kernel driver.
if [ -c /dev/sgx_provision -o -c /dev/sgx/provision ]; then
    /usr/bin/getent group sgx_prv &> /dev/null || /usr/sbin/groupadd sgx_prv
    trigger_udev
fi

%changelog
* Thu Dec 9 2021 Yunying Sun <yunying.sun@intel.com> - 2.15.100.0-1 
- Initial packaging
