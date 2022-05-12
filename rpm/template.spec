%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-rclc-parameter
Version:        4.0.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rclc_parameter package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-builtin-interfaces
Requires:       ros-humble-rcl
Requires:       ros-humble-rcl-interfaces
Requires:       ros-humble-rclc
Requires:       ros-humble-rcutils
Requires:       ros-humble-rosidl-runtime-c
Requires:       ros-humble-ros-workspace
BuildRequires:  ros-humble-ament-cmake-gtest
BuildRequires:  ros-humble-ament-cmake-pytest
BuildRequires:  ros-humble-ament-cmake-ros
BuildRequires:  ros-humble-ament-lint-auto
BuildRequires:  ros-humble-ament-lint-common
BuildRequires:  ros-humble-builtin-interfaces
BuildRequires:  ros-humble-example-interfaces
BuildRequires:  ros-humble-osrf-testing-tools-cpp
BuildRequires:  ros-humble-rcl
BuildRequires:  ros-humble-rcl-interfaces
BuildRequires:  ros-humble-rclc
BuildRequires:  ros-humble-rclcpp
BuildRequires:  ros-humble-rcutils
BuildRequires:  ros-humble-rosidl-runtime-c
BuildRequires:  ros-humble-std-msgs
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Parameter server implementation for micro-ROS nodes

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Thu May 12 2022 Antonio Cuadros <antoniocuadros@eprosima.com> - 4.0.0-1
- Autogenerated by Bloom

* Tue Apr 19 2022 Antonio Cuadros <antoniocuadros@eprosima.com> - 3.0.8-2
- Autogenerated by Bloom

* Thu Apr 14 2022 Antonio Cuadros <antoniocuadros@eprosima.com> - 3.0.8-1
- Autogenerated by Bloom

* Thu Feb 17 2022 Antonio Cuadros <antoniocuadros@eprosima.com> - 3.0.7-1
- Autogenerated by Bloom

* Tue Feb 08 2022 Antonio Cuadros <antoniocuadros@eprosima.com> - 3.0.6-2
- Autogenerated by Bloom

