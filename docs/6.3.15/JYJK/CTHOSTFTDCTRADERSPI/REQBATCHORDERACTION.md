<p>批量报单操作请求</p>
<p>错误回报: OnErrRtnBatchOrderAction，OnRspBatchOrderAction</p>
<p>正确回报：OnRtnOrder</p>
<span class="anchor" id="12d68ee0-303c-49d9-b808-5bdde174b7ca"></span>
## 1.函数原型
<p>virtual int ReqBatchOrderAction(CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, int nRequestID) = 0;</p>
<span class="anchor" id="258fb9be-1b70-4c88-9979-ce85dd589d9b"></span>
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
<span class="anchor" id="36cf3610-be76-4cbe-bced-9dcbb48371b6"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="371b60d9-3ba9-4623-88c6-4e8347567782"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="16e404cd-c9fe-4b4b-acee-d74c95392502"></span>
## 5.FAQ
<p>无</p>
