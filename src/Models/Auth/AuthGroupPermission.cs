using System;
using System.Collections.Generic;

#nullable disable

namespace ComicBookTracker
{
    public partial class AuthGroupPermission
    {
        public long Id { get; set; }
        public long GroupId { get; set; }
        public long PermissionId { get; set; }

        public virtual AuthGroup Group { get; set; }
        public virtual AuthPermission Permission { get; set; }
    }
}
