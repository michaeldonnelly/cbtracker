using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;

#nullable disable

namespace ComicBookTracker.Models
{
    [Table("cbtracker_series")]
    public partial class Series
    {
        public Series()
        {
            Issues = new HashSet<Issue>();
            SeriesTags = new HashSet<SeriesTag>();
            //Trades = new HashSet<Trade>();
        }

        public long Id { get; set; }
        public string Name { get; set; }
        public long? Volume { get; set; }

        [Column("start_year")]
        public long StartYear { get; set; }
        public bool Current { get; set; }
        public DateTime Updated { get; set; }
        public DateTime Created { get; set; }

        [Column("author_id")]
        public long? AuthorId { get; set; }

        [Column("publisher_id")]
        public long? PublisherId { get; set; }
        [Column("sort_name")]
        public string SortName { get; set; }
        public bool PullList { get; set; }

        public virtual Author Author { get; set; }
        public virtual Publisher Publisher { get; set; }
        public virtual ICollection<Issue> Issues { get; set; }
        public virtual ICollection<SeriesTag> SeriesTags { get; set; }
        public virtual ICollection<Tag> Tags { get; set; }
        public virtual ICollection<Trade> Trades { get; set; }

        public override string ToString()
        {
            return String.Format("{0} ({1})", Name, StartYear.ToString());
        }

        public string Sortable()
        {
            return String.Format("{0}-{1}-{2}", SortName, StartYear, Volume);
        }
    }
}
