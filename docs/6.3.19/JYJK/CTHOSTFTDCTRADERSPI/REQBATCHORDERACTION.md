<p>批量报单操作请求</p>
<p>错误回报: OnErrRtnBatchOrderAction，OnRspBatchOrderAction</p>
<p>正确回报：OnRtnOrder</p>
<span class="anchor" id="36d9aaed-90f6-4126-b992-281a79d77700"></span>
## 1.函数原型
<p>virtual int ReqBatchOrderAction(CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, int nRequestID) = 0;</p>
<span class="anchor" id="a70f06fc-6a03-4ec3-a25b-40efe2786e4d"></span>
## 2.参数
<p>pInputBatchOrderAction：输入批量报单操作</p>
<pre><code>struct CThostFtdcInputBatchOrderActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///报单操作引用
    TThostFtdcOrderActionRefType OrderActionRef;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///前置编号
    TThostFtdcFrontIDType FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="b4b8abec-f7fb-4970-a1ff-f612c66c1d33"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="da725953-0322-4497-bac2-4c0e7cd4117a"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="245233fc-bcd6-4924-9062-a644d05a798e"></span>
## 5.FAQ
<p>无</p>
