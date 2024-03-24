<p>交易通知，无Req属于私有流回报。</p>
<span class="anchor" id="70f57f68-22af-4e62-b827-311deb9ea1fa"></span>
## 1.函数原型
<p>virtual void OnRtnTradingNotice(CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo) {};</p>
<span class="anchor" id="389fa065-e43e-4860-8ea4-334cbeb463c4"></span>
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
<span class="anchor" id="b2dfc8b2-ee02-4a55-a0d9-779cecf8ad42"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="3c40010c-4725-4bce-a484-7350fe5ec775"></span>
## 4.FAQ
<p>无</p>
