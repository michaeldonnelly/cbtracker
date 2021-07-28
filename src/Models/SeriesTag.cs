using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;

#nullable disable

namespace ComicBookTracker.Models
{
    [Table("cbtracker_series_tags")]
    public partial class SeriesTag
    {
        public long Id { get; set; }
        [Column("series_id")]
        public long SeriesId { get; set; }
        [Column("tag_id")]
        public long TagId { get; set; }

        public virtual Series Series { get; set; }
        public virtual Tag Tag { get; set; }
    }
}
