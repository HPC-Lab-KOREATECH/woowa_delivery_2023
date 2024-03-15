# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_artificial_occupy_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED artificial_occupy_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(artificial_occupy_FOUND FALSE)
  elseif(NOT artificial_occupy_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(artificial_occupy_FOUND FALSE)
  endif()
  return()
endif()
set(_artificial_occupy_CONFIG_INCLUDED TRUE)

# output package information
if(NOT artificial_occupy_FIND_QUIETLY)
  message(STATUS "Found artificial_occupy: 1.0.0 (${artificial_occupy_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'artificial_occupy' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${artificial_occupy_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(artificial_occupy_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${artificial_occupy_DIR}/${_extra}")
endforeach()
