<p>交易通知，无Req属于私有流回报。</p>
<span class="anchor" id="90de80a6-5685-4a18-ab71-0986e2c4fb00"></span>
## 1.函数原型
<p>virtual void OnRtnTradingNotice(CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo) {};</p>
<span class="anchor" id="8c86331a-bdf2-48b2-9e68-9545d9e09f33"></span>
## 2.参数
<p>pTradingNoticeInfo：用户事件通知信息</p>
<pre><code>struct CThostFtdcTradingNoticeInfoField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///发送时间
    TThostFtdcTimeType SendTime;
    ///消息正文
    TThostFtdcContentType FieldContent;
    ///序列系列号
    TThostFtdcSequenceSeriesType SequenceSeries;
    ///序列号
    TThostFtdcSequenceNoType SequenceNo;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<span class="anchor" id="2b6e53f5-8130-4b10-b901-3a785c85ac05"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="f29265ed-3d59-43c8-9fee-3f436db860c5"></span>
## 4.FAQ
<p>无</p>
