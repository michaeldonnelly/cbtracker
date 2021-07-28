using System;
using System.Collections.Generic;

#nullable disable

namespace ComicBookTracker
{
    public partial class AuthUserGroup
    {
        public long Id { get; set; }
        public long UserId { get; set; }
        public long GroupId { get; set; }

        public virtual AuthGroup Group { get; set; }
        public virtual AuthUser User { get; set; }
    }
}
