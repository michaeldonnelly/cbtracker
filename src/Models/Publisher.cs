using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;

#nullable disable

namespace ComicBookTracker.Models
{
    [Table("cbtracker_publisher")]
    public partial class Publisher
    {
        public Publisher()
        {
            Issues = new HashSet<Issue>();
            Series = new HashSet<Series>();
            InverseImprintOf = new HashSet<Publisher>();
        }

        public long Id { get; set; }
        public string Name { get; set; }

        [Column("imprint_of_id")]
        public long? ImprintOfId { get; set; }
        public DateTime Updated { get; set; }
        public DateTime Created { get; set; }

        public virtual Publisher ImprintOf { get; set; }
        public virtual ICollection<Issue> Issues { get; set; }
        public virtual ICollection<Series> Series { get; set; }
        public virtual ICollection<Publisher> InverseImprintOf { get; set; }
    }
}
