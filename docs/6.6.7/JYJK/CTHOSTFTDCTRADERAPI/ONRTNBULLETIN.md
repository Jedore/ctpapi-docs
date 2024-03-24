<p>交易所公告通知，无Req属于公有流回报</p>
<span class="anchor" id="f48080fa-6bb5-4fc6-8058-139b2ea19ede"></span>
## 1.函数原型
<p>virtual void OnRtnBulletin(CThostFtdcBulletinField *pBulletin) {};</p>
<span class="anchor" id="bdcda840-93d9-49c9-a5a9-3f437fd06275"></span>
## 2.参数
<p>pBulletin：交易所公告</p>
<pre><code>struct CThostFtdcBulletinField
{
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///交易日
    TThostFtdcDateType TradingDay;
    ///公告编号
    TThostFtdcBulletinIDType BulletinID;
    ///序列号
    TThostFtdcSequenceNoType SequenceNo;
    ///公告类型
    TThostFtdcNewsTypeType NewsType;
    ///紧急程度
    TThostFtdcNewsUrgencyType NewsUrgency;
    ///发送时间
    TThostFtdcTimeType SendTime;
    ///消息摘要
    TThostFtdcAbstractType Abstract;
    ///消息来源
    TThostFtdcComeFromType ComeFrom;
    ///消息正文
    TThostFtdcContentType Content;
    ///WEB地址
    TThostFtdcURLLinkType URLLink;
    ///市场代码
    TThostFtdcMarketIDType MarketID;
};
</code></pre>
<span class="anchor" id="484713bc-0752-4346-8d4f-f809c5ca9430"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="3a319505-fcaa-418c-9873-4a607a643ddb"></span>
## 4.FAQ
<p>无</p>
