using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;

#nullable disable

namespace ComicBookTracker.Models
{
    [Table("cbtracker_trade")]
    public partial class Trade
    {
        public long Id { get; set; }
        public long Volume { get; set; }
        public bool Own { get; set; }
        public string Title { get; set; }

        [Column("release_month")]
        public long? ReleaseMonth { get; set; }

        [Column("release_year")]
        public long? ReleaseYear { get; set; }
        public Binding Binding { get; set; }

        [Column("series_id")]
        public long SeriesId { get; set; }

        public virtual Series Series { get; set; }
    }

    public enum Binding
    {
        Paperback = 0,
        Hardcover = 1
    }
}
