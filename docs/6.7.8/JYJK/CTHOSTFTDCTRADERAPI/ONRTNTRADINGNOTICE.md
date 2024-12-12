<p>交易通知，无Req属于私有流回报。</p>
<p><span alt="" id="anchor-id-01"></span> </p>
<p>注：风控终端发送的风险通知由此接口接收。</p>
<span class="anchor" id="30c3a573-5bb1-415e-b157-cefc0488e509"></span>
## 1.函数原型
<p>virtual void OnRtnTradingNotice(CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo) {};</p>
<span class="anchor" id="7c2ff09b-17f5-48da-bd43-b81b52dc316a"></span>
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
<span class="anchor" id="5c04070e-f1e3-45a7-9ec2-9d299f2cc04b"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="6389a018-34df-470d-9c6a-6ee32e39bc63"></span>
## 4.FAQ
<p>无</p>
