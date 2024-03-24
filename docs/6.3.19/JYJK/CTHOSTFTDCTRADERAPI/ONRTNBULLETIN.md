<p>交易所公告通知，无Req属于私有流回报</p>
<span class="anchor" id="29f42c6a-9496-42a3-b4b1-232664dbd1cd"></span>
## 1.函数原型
<p>virtual void OnRtnBulletin(CThostFtdcBulletinField *pBulletin) {};</p>
<span class="anchor" id="afeccc32-f2e2-484a-b282-6975ab329da8"></span>
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
<span class="anchor" id="dd2e0c9a-17f8-491f-94d1-933e462274ae"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="8e81d377-c216-4a1c-94f0-b3d131a322b4"></span>
## 4.FAQ
<p>无</p>
