using System;
using System.Collections.Generic;

#nullable disable

namespace ComicBookTracker.Models
{
    public partial class Favorite
    {
        public long Id { get; set; }
        public string Name { get; set; }
        public byte[] Updated { get; set; }
        public byte[] Created { get; set; }
        public string RelativeUrl { get; set; }
    }
}
