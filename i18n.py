#
# Project Kimchi
#
# Copyright IBM, Corp. 2014-2015
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA

import gettext

_ = gettext.gettext


messages = {
    "KCHAPI0001E": _("Unknown parameter %(value)s"),

    "KCHAUTH0004E": _("User %(user_id)s not found with given LDAP settings."),

    "KCHDISKS0001E": _("Error while getting block devices. Details: %(err)s"),
    "KCHDISKS0002E": _("Error while getting block device information for %(device)s."),

    "KCHLVM0001E": _("Unable to retrieve LVM information. Details: %(err)s"),

    "KCHPART0001E": _("Partition %(name)s does not exist in the host"),

    "KCHDEVS0001E": _('Unknown "_cap" specified'),
    "KCHDEVS0002E": _('"_passthrough" should be "true" or "false"'),
    "KCHDEVS0003E": _('"_passthrough_affected_by" should be a device name string'),
    "KCHDEVS0004E": _('"_available_only" should be "true" or "false"'),

    "KCHDL0001E": _("Unable to find distro file: %(filename)s"),
    "KCHDL0002E": _("Unable to parse distro file: %(filename)s. Make sure, it is a JSON file."),

    "KCHISCSI0001E": _("Unable to login to iSCSI host target %(portal)s. Details: %(err)s"),
    "KCHISCSI0002E": _("Unable to login to iSCSI host %(host)s target %(target)s"),

    "KCHISO0001E": _("Unable to find ISO file %(filename)s"),
    "KCHISO0002E": _("The ISO file %(filename)s is not bootable"),
    "KCHISO0003E": _("The ISO file %(filename)s does not have a valid El Torito boot record"),
    "KCHISO0004E": _("Invalid El Torito validation entry in ISO %(filename)s"),
    "KCHISO0005E": _("Invalid El Torito boot indicator in ISO %(filename)s"),
    "KCHISO0006E": _("Unexpected volume type for primary volume in ISO %(filename)s"),
    "KCHISO0007E": _("Bad format while reading volume descriptor in ISO %(filename)s"),
    "KCHISO0008E": _("The hypervisor doesn't have permission to use this ISO %(filename)s. "
                     "Consider moving it under /var/lib/libvirt,  or set the search permission "
                     "to file access control lists for '%(user)s' user if possible, or add the "
                     "'%(user)s' to the ISO path group, or (not recommended) 'chmod -R o+x 'path_to_iso'."
                     "Details: %(err)s" ),

    "KCHIMG0001E": _("An error occurred when probing image OS information."),
    "KCHIMG0003E": _("Unable to read image file %(filename)s"),
    "KCHIMG0004E": _("Image file must be an existing file on system. %(filename)s is not a valid input."),

    "KCHVM0001E": _("Virtual machine %(name)s already exists"),
    "KCHVM0002E": _("Virtual machine %(name)s does not exist"),
    "KCHVM0003E": _("Unable to rename virtual machine %(name)s. The name %(new_name)s is already in use or the virtual machine is not powered off."),
    "KCHVM0004E": _("Unable to retrieve screenshot for stopped virtual machine %(name)s"),
    "KCHVM0005E": _("Remote ISO image is not supported by this server."),
    "KCHVM0006E": _("Screenshot is not supported on virtual machine %(name)s"),
    "KCHVM0007E": _("Unable to create virtual machine %(name)s. Details: %(err)s"),
    "KCHVM0008E": _("Unable to update virtual machine %(name)s. Details: %(err)s"),
    "KCHVM0009E": _("Unable to retrieve virtual machine %(name)s. Details: %(err)s"),
    "KCHVM0010E": _("Unable to connect to powered off virtual machine %(name)s."),
    "KCHVM0011E": _("Virtual machine name must be a string without slashes (/)"),
    "KCHVM0012E": _("Invalid template URI %(value)s specified for virtual machine"),
    "KCHVM0013E": _("Invalid storage pool URI %(value)s specified for virtual machine"),
    "KCHVM0014E": _("Supported virtual machine graphics are Spice or VNC"),
    "KCHVM0015E": _("Graphics address to listen on must be IPv4 or IPv6"),
    "KCHVM0016E": _("Specify a template to create a virtual machine from"),
    "KCHVM0019E": _("Unable to start virtual machine %(name)s. Details: %(err)s"),
    "KCHVM0020E": _("Unable to power off virtual machine %(name)s. Details: %(err)s"),
    "KCHVM0021E": _("Unable to delete virtual machine %(name)s. Details: %(err)s"),
    "KCHVM0022E": _("Unable to reset virtual machine %(name)s. Details: %(err)s"),
    "KCHVM0023E": _("User name list must be an array"),
    "KCHVM0024E": _("User name must be a string"),
    "KCHVM0025E": _("Group name list must be an array"),
    "KCHVM0026E": _("Group name must be a string"),
    "KCHVM0027E": _("User(s) '%(users)s' do not exist"),
    "KCHVM0028E": _("Group(s) '%(groups)s' do not exist"),
    "KCHVM0029E": _("Unable to shutdown virtual machine %(name)s. Details: %(err)s"),
    "KCHVM0031E": _("The guest console password must be a string."),
    "KCHVM0032E": _("The life time for the guest console password must be a number."),
    "KCHVM0033E": _("Virtual machine '%(name)s' must be stopped before cloning it."),
    "KCHVM0034E": _("Insufficient disk space to clone virtual machine '%(name)s'"),
    "KCHVM0035E": _("Unable to clone VM '%(name)s'. Details: %(err)s"),
    "KCHVM0036E": _("Invalid operation for non-persistent virtual machine %(name)s"),
    "KCHVM0037E": _("Cannot suspend VM '%(name)s' because it is not running."),
    "KCHVM0038E": _("Unable to suspend VM '%(name)s'. Details: %(err)s"),
    "KCHVM0039E": _("Cannot resume VM '%(name)s' because it is not paused."),
    "KCHVM0040E": _("Unable to resume VM '%(name)s'. Details: %(err)s"),
    "KCHVM0041E": _("Memory assigned is higher then the maximum allowed in the host: %(maxmem)sMib."),
    "KCHVM0042E": _("VM '%(name)s' does not support live memory update. Update the memory with the machine offline to enable this feature."),
    "KCHVM0043E": _("Only increase memory is allowed in active VMs"),
    "KCHVM0044E": _("For live memory update, new memory value must be equal old memory value plus multiples of 1024 Mib"),
    "KCHVM0045E": _("There are not enough free slots of 1024 Mib in the guest."),
    "KCHVM0046E": _("Host's libvirt version does not support memory devices. Libvirt must be >= 1.2.14"),
    "KCHVM0047E": _("Error attaching memory device. Details: %(error)s"),
    "KCHVM0048E": _("Cannot start %(name)s. Virtual machine is already running."),
    "KCHVM0049E": _("Cannot power off %(name)s. Virtual machine is shut off."),
    "KCHVM0050E": _("Cannot shutdown %(name)s. Virtual machine is shut off."),
    "KCHVM0051E": _("Cannot reset %(name)s. Virtual machine is already shut off."),

    "KCHVM0055E": _("Migrate to localhost %(host)s is not allowed."),
    "KCHVM0056E": _("To migrate a virtual machine to the remote host %(host)s the user %(user)s must have password-less login to the remote host."),
    "KCHVM0057E": _("Can not migrate virtual machine %(name)s when its in %(state)s state."),
    "KCHVM0058E": _("Failed to migrate virtual machine %(name)s due error: %(err)s"),
    "KCHVM0059E": _("User name of the remote server must be a string."),
    "KCHVM0060E": _("Destination host of the migration must be a string."),
    "KCHVM0061E": _("Unable to create file %(path)s at %(host)s using user %(user)s."),
    "KCHVM0062E": _("Unable to read disk size of %(path)s, error: %(error)s"),
    "KCHVM0063E": _("Unable to create disk image %(path)s at %(host)s using user %(user)s. Error: %(error)s"),
    "KCHVM0064E": _("Unable to migrate virtual machine to remote host %(host)s with arch %(destarch)s using localhost with arch %(srcarch)s."),
    "KCHVM0065E": _("Unable to migrate virtual machine to remote host %(host)s with hypervisor %(desthyp)s because localhost uses hypervisor %(srchyp)s."),
    "KCHVM0066E": _("Unable to determine remote host hypervisor and architecture. Error: %(error)s"),
    "KCHVM0067E": _("Unable to migrate virtual machine: subcores per core setting from localhostand remote host %(host)s differs."),
    "KCHVM0068E": _("Unable to setup password-less login at remote host %(host)s using user %(user)s. Error: %(error)s"),
    "KCHVM0069E": _("Password field must be a string."),
    "KCHVM0070E": _("Error creating local host ssh rsa key of user 'root'."),
    "KCHVM0071E": _("Memory value %(mem)s must be aligned to %(alignment)sMiB."),
    "KCHVM0073E": _("Unable to update the following parameters while the VM is offline: %(params)s"),
    "KCHVM0074E": _("Unable to update the following parameters while the VM is online: %(params)s"),
    "KCHVM0075E": _("Cannot change VCPU value because '%(vm)s' has a topology defined - sockets: %(sockets)s, cores: %(cores)s, threads: %(threads)s."),

    "KCHVMHDEV0001E": _("VM %(vmid)s does not contain directly assigned host device %(dev_name)s."),
    "KCHVMHDEV0002E": _("The host device %(dev_name)s is not allowed to directly assign to VM."),
    "KCHVMHDEV0003E": _("No IOMMU groups found. Host PCI pass through needs IOMMU group to function correctly. "
                        "Please enable Intel VT-d or AMD IOMMU in your BIOS, then verify the Kernel is compiled with IOMMU support. "
                        "For Intel CPU, add intel_iommu=on to your Kernel parameter in /boot/grub2/grub.conf. "
                        "For AMD CPU, add iommu=pt iommu=1."),
    "KCHVMHDEV0004E": _('"name" should be a device name string'),
    "KCHVMHDEV0005E": _('The device %(name)s is probably in use by the host. Unable to attach it to the guest.'),

    "KCHVMIF0001E": _("Interface %(iface)s does not exist in virtual machine %(name)s"),
    "KCHVMIF0002E": _("Network %(network)s specified for virtual machine %(name)s does not exist"),
    "KCHVMIF0004E": _("Supported virtual machine interfaces type is only network"),
    "KCHVMIF0005E": _("Network name for virtual machine interface must be a string"),
    "KCHVMIF0006E": _("Invalid network model card specified for virtual machine interface"),
    "KCHVMIF0007E": _("Specify type and network to add a new virtual machine interface"),
    "KCHVMIF0008E": _("MAC Address must respect this format FF:FF:FF:FF:FF:FF"),
    "KCHVMIF0009E": _("MAC Address %(mac)s already exists in virtual machine %(name)s"),
    "KCHVMIF0010E": _("Invalid MAC Address"),
    "KCHVMIF0011E": _("Cannot change MAC address of a running virtual machine"),

    "KCHTMPL0001E": _("Template %(name)s already exists"),
    "KCHTMPL0003E": _("Network '%(network)s' specified for template %(template)s does not exist"),
    "KCHTMPL0004E": _("Storage pool %(pool)s specified for template %(template)s does not exist"),
    "KCHTMPL0005E": _("Storage pool %(pool)s specified for template %(template)s is not active"),
    "KCHTMPL0006E": _("Invalid parameter '%(param)s' specified for CDROM."),
    "KCHTMPL0007E": _("Network %(network)s specified for template %(template)s is not active"),
    "KCHTMPL0008E": _("Template name must be a string"),
    "KCHTMPL0009E": _("Template icon must be a path to the image"),
    "KCHTMPL0010E": _("Template distribution must be a string"),
    "KCHTMPL0011E": _("Template distribution version must be a string"),
    "KCHTMPL0012E": _("The number of CPUs must be an integer greater than 0"),
    "KCHTMPL0013E": _("Amount of memory (MB) must be an integer greater than 512"),
    "KCHTMPL0014E": _("Template CDROM must be a local or remote ISO file"),
    "KCHTMPL0015E": _("Invalid storage pool URI %(value)s specified for template"),
    "KCHTMPL0016E": _("Specify an ISO image as CDROM or a base image to create a template"),
    "KCHTMPL0017E": _("All networks for the template must be specified in a list."),
    "KCHTMPL0018E": _("Specify a volume to a template when storage pool is iSCSI or SCSI"),
    "KCHTMPL0019E": _("The volume %(volume)s is not in storage pool %(pool)s"),
    "KCHTMPL0020E": _("Unable to create template due error: %(err)s"),
    "KCHTMPL0021E": _("Unable to delete template due error: %(err)s"),
    "KCHTMPL0022E": _("Disk size must be an integer greater than 1GB."),
    "KCHTMPL0023E": _("Template base image must be a valid local image file"),
    "KCHTMPL0024E": _("Cannot identify base image %(path)s format"),
    "KCHTMPL0025E": _("When specifying CPU topology, VCPUs must be a product of sockets, cores, and threads."),
    "KCHTMPL0026E": _("When specifying CPU topology, each element must be an integer greater than zero."),
    "KCHTMPL0027E": _("Invalid disk image format. Valid formats: bochs, cloop, cow, dmg, qcow, qcow2, qed, raw, vmdk, vpc."),
    "KCHTMPL0028E": _("When setting template disks, following parameters are required: 'index', 'pool name', 'format', 'size' or 'volume' (for scsi/iscsi pools)"),
    "KCHTMPL0029E": _("Disk format must be 'raw', for logical, iscsi, and scsi pools."),

    "KCHPOOL0001E": _("Storage pool %(name)s already exists"),
    "KCHPOOL0002E": _("Storage pool %(name)s does not exist"),
    "KCHPOOL0004E": _("Specify %(item)s in order to create the storage pool %(name)s"),
    "KCHPOOL0005E": _("Unable to delete active storage pool %(name)s"),
    "KCHPOOL0006E": _("Unable to list storage pools. Details: %(err)s"),
    "KCHPOOL0007E": _("Unable to create storage pool %(name)s. Details: %(err)s"),
    "KCHPOOL0008E": _("Unable to get number of storage volumes in storage pool %(name)s. Details: %(err)s"),
    "KCHPOOL0009E": _("Unable to activate storage pool %(name)s. Details: %(err)s"),
    "KCHPOOL0010E": _("Unable to deactivate storage pool %(name)s. Details: %(err)s"),
    "KCHPOOL0011E": _("Unable to delete storage pool %(name)s. Details: %(err)s"),
    "KCHPOOL0012E": _("Unable to create NFS Pool as export path %(path)s may block during mount"),
    "KCHPOOL0013E": _("Unable to create NFS Pool as export path %(path)s mount failed"),
    "KCHPOOL0014E": _("Unsupported storage pool type: %(type)s"),
    "KCHPOOL0015E": _("Error while retrieving storage pool XML to %(pool)s"),
    "KCHPOOL0016E": _("Storage pool name must be a string without slashes (/)"),
    "KCHPOOL0017E": _("Supported storage pool types are dir, netfs, logical, iscsi, isci and kimchi-iso"),
    "KCHPOOL0018E": _("Storage pool path must be a string"),
    "KCHPOOL0019E": _("Storage pool host must be a IP or hostname"),
    "KCHPOOL0020E": _("Storage pool device must be the absolute path to the block device"),
    "KCHPOOL0021E": _("Storage pool devices parameter must be a list"),
    "KCHPOOL0022E": _("Target IQN of an iSCSI pool must be a string"),
    "KCHPOOL0023E": _("Port of a remote storage server must be an integer between 1 and 65535"),
    "KCHPOOL0024E": _("iSCSI target username must be a string"),
    "KCHPOOL0025E": _("iSCSI target password must be a string"),
    "KCHPOOL0026E": _("Specify name and type to create a storage pool"),
    "KCHPOOL0027E": _("%(disk)s is not a valid disk/partition. Could not add it to the pool %(pool)s."),
    "KCHPOOL0028E": _("Unable to extend logical pool %(pool)s. Details: %(err)s"),
    "KCHPOOL0029E": _("The parameter disks only can be updated for logical storage pool."),
    "KCHPOOL0030E": _("The SCSI host adapter name must be a string."),
    "KCHPOOL0031E": _("The storage pool kimchi_isos is reserved for internal use"),
    "KCHPOOL0032E": _("Unable to activate NFS storage pool %(name)s. NFS server %(server)s is unreachable."),
    "KCHPOOL0033E": _("Unable to deactivate NFS storage pool %(name)s. NFS server %(server)s is unreachable."),
    "KCHPOOL0034E": _("Unable to deactivate pool %(name)s as it is associated with some templates"),
    "KCHPOOL0035E": _("Unable to delete pool %(name)s as it is associated with some templates"),
    "KCHPOOL0036E": _("A volume group named '%(name)s' already exists. Please, choose another name to create the logical pool."),
    "KCHPOOL0037E": _("Unable to update database with deep scan information due error: %(err)s"),
    "KCHPOOL0038E": _("No volume group '%(name)s' found. Please, specify an existing volume group to create the logical pool from."),

    "KCHVOL0001E": _("Storage volume %(name)s already exists"),
    "KCHVOL0002E": _("Storage volume %(name)s does not exist in storage pool %(pool)s"),
    "KCHVOL0003E": _("Unable to create storage volume %(volume)s because storage pool %(pool)s is not active"),
    "KCHVOL0004E": _("Specify %(item)s in order to create storage volume %(volume)s"),
    "KCHVOL0006E": _("Unable to list storage volumes because storage pool %(pool)s is not active"),
    "KCHVOL0007E": _("Unable to create storage volume %(name)s in storage pool %(pool)s. Details: %(err)s"),
    "KCHVOL0008E": _("Unable to list storage volumes in storage pool %(pool)s. Details: %(err)s"),
    "KCHVOL0009E": _("Unable to wipe storage volumes %(name)s. Details: %(err)s"),
    "KCHVOL0010E": _("Unable to delete storage volume %(name)s. Details: %(err)s"),
    "KCHVOL0011E": _("Unable to resize storage volume %(name)s. Details: %(err)s"),
    "KCHVOL0012E": _("Storage type %(type)s does not support volume create and delete"),
    "KCHVOL0013E": _("Storage volume name must be a string"),
    "KCHVOL0014E": _("Storage volume allocation must be an integer number"),
    "KCHVOL0015E": _("Storage volume format not supported. Valid formats: bochs, cloop, cow, dmg, qcow, qcow2, qed, raw, vmdk, vpc."),
    "KCHVOL0016E": _("Storage volume requires a volume name"),
    "KCHVOL0017E": _("Unable to update database with storage volume information due error: %(err)s"),
    "KCHVOL0018E": _("Only one of parameter %(param)s can be specified"),
    "KCHVOL0019E": _("Create volume from %(param)s is not supported"),
    "KCHVOL0020E": _("Storage volume capacity must be an integer number."),
    "KCHVOL0021E": _("Storage volume URL must be http://, https://, ftp:// or ftps://."),
    "KCHVOL0022E": _("Unable to access file %(url)s. Please, check it."),
    "KCHVOL0023E": _("Unable to clone storage volume '%(name)s' in pool '%(pool)s'. Details: %(err)s"),
    "KCHVOL0024E": _("Specify chunk data and its size to upload a file."),
    "KCHVOL0025E": _("In order to upload a storage volume, specify the 'upload' parameter."),
    "KCHVOL0026E": _("Unable to upload chunk data as it does not match with requested chunk size."),
    "KCHVOL0027E": _("The storage volume %(vol)s is not under an upload process."),
    "KCHVOL0028E": _("The upload chunk data will exceed the storage volume size."),
    "KCHVOL0029E": _("Unable to upload chunk data to storage volume. Details: %(err)s."),

    "KCHIFACE0001E": _("Interface %(name)s does not exist"),

    "KCHNET0001E": _("Network %(name)s already exists"),
    "KCHNET0002E": _("Network %(name)s does not exist"),
    "KCHNET0003E": _("Subnet %(subnet)s specified for network %(network)s  is not valid."),
    "KCHNET0004E": _("Specify a network interface to create bridged network %(name)s"),
    "KCHNET0005E": _("Unable to delete active network %(name)s"),
    "KCHNET0006E": _("Interface %(iface)s specified for network %(network)s is already in use"),
    "KCHNET0007E": _("Interface should be bare NIC, bonding or bridge device."),
    "KCHNET0008E": _("Unable to create network %(name)s. Details: %(err)s"),
    "KCHNET0009E": _("Unable to find a free IP address for network '%(name)s'"),
    "KCHNET0010E": _("The interface %(iface)s already exists."),
    "KCHNET0011E": _("Network name must be a string without slashes (/) or quotes (\")"),
    "KCHNET0012E": _("Supported network types are isolated, NAT, macvtap and bridge"),
    "KCHNET0013E": _("Network subnet must be a string with IP address and prefix or netmask"),
    "KCHNET0014E": _("Network interface must be a string"),
    "KCHNET0015E": _("Network VLAN ID must be an integer between 1 and 4094"),
    "KCHNET0016E": _("Specify name and type to create a Network"),
    "KCHNET0017E": _("Unable to delete network %(name)s. There are some virtual machines %(vms)s and/or templates linked to this network."),
    "KCHNET0018E": _("Unable to deactivate network %(name)s. There are some virtual machines %(vms)s and/or templates linked to this network."),
    "KCHNET0019E": _("Bridge device %(name)s can not be the trunk device of a VLAN."),
    "KCHNET0020E": _("Failed to activate interface %(iface)s: %(err)s."),
    "KCHNET0021E": _("Failed to activate interface %(iface)s. Please check the physical link status."),
    "KCHNET0022E": _("Failed to start network %(name)s. Details: %(err)s"),
    "KCHNET0024E": _("Unable to redefine interface %(name)s. Details: %(err)s"),
    "KCHNET0025E": _("Unable to create bridge %(name)s. Details: %(err)s"),
    "KCHNET0026E": _("Open VSwitch bridges can only host bridged networks."),

    "KCHSR0001E": _("Storage server %(server)s was not used by Kimchi"),

    "KCHDISTRO0001E": _("Distro '%(name)s' does not exist"),

    "KCHHOST0003E": _("Node device '%(name)s' not found"),
    "KCHHOST0004E": _("Conflicting flag filters specified."),

    "KCHUTILS0003E": _("Unable to choose a virtual machine name"),
    "KCHUTILS0006E": _("Cannot upgrade objectstore data."),

    "KCHVMSTOR0002E": _("Invalid storage type. Types supported: 'cdrom', 'disk'"),
    "KCHVMSTOR0003E": _("The path '%(value)s' is not a valid local/remote path for the device"),
    "KCHVMSTOR0006E": _("Only CDROM path can be update."),
    "KCHVMSTOR0007E": _("The storage device %(dev_name)s does not exist in the virtual machine %(vm_name)s"),
    "KCHVMSTOR0008E": _("Error while creating new storage device: %(error)s"),
    "KCHVMSTOR0009E": _("Error while updating storage device: %(error)s"),
    "KCHVMSTOR0010E": _("Error while removing storage device: %(error)s"),
    "KCHVMSTOR0011E": _("Do not support IDE device hot plug"),
    "KCHVMSTOR0012E": _("Specify type and path or type and pool/volume to add a new virtual machine disk"),
    "KCHVMSTOR0013E": _("Specify path to update virtual machine disk"),
    "KCHVMSTOR0014E": _("Controller type %(type)s limitation of %(limit)s devices reached"),
    "KCHVMSTOR0015E": _("Cannot retrieve disk path information for given pool/volume: %(error)s"),
    "KCHVMSTOR0016E": _("Volume already in use by other virtual machine."),
    "KCHVMSTOR0017E": _("Only one of path or pool/volume can be specified to add a new virtual machine disk"),
    "KCHVMSTOR0018E": _("Volume chosen with format %(format)s does not fit in the storage type %(type)s"),

    "KCHSNAP0001E": _("Virtual machine '%(vm)s' must be stopped before creating a snapshot of it."),
    "KCHSNAP0002E": _("Unable to create snapshot '%(name)s' on virtual machine '%(vm)s'. Details: %(err)s"),
    "KCHSNAP0003E": _("Snapshot '%(name)s' does not exist on virtual machine '%(vm)s'."),
    "KCHSNAP0004E": _("Unable to retrieve snapshot '%(name)s' on virtual machine '%(vm)s'. Details: %(err)s"),
    "KCHSNAP0005E": _("Unable to list snapshots on virtual machine '%(vm)s'. Details: %(err)s"),
    "KCHSNAP0006E": _("Unable to delete snapshot '%(name)s' on virtual machine '%(vm)s'. Details: %(err)s"),
    "KCHSNAP0008E": _("Unable to retrieve current snapshot of virtual machine '%(vm)s'. Details: %(err)s"),
    "KCHSNAP0009E": _("Unable to revert virtual machine '%(vm)s' to snapshot '%(name)s'. Details: %(err)s"),
    "KCHSNAP0010E": _("Unable to create snapshot of virtual machine '%(vm)s' because it contains a disk with format '%(format)s'; only 'qcow2' is supported."),

    "KCHCPUINF0001E": _("The number of vCPUs is too large for this system."),
    "KCHCPUINF0002E": _("Invalid vCPU/topology combination."),
    "KCHCPUINF0003E": _("This host (or current configuration) does not allow CPU topology."),

    "KCHLVMS0001E": _("Invalid volume group name parameter: %(name)s."),

}
