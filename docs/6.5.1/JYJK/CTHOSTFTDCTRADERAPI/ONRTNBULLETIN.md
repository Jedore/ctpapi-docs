<p>交易所公告通知，无Req属于公有流回报</p>
<span class="anchor" id="97643dac-51ed-4407-8ab8-702eeff82056"></span>
## 1.函数原型
<p>virtual void OnRtnBulletin(CThostFtdcBulletinField *pBulletin) {};</p>
<span class="anchor" id="0a58d996-9e1e-42b2-9a4c-a547dc7144da"></span>
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
<span class="anchor" id="99f82263-a3eb-4fd1-af4d-a14f3de64abf"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="8d4bdb82-f7c2-40ad-960e-2de538f1475e"></span>
## 4.FAQ
<p>无</p>
