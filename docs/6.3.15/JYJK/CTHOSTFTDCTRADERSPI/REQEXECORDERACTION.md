<p>执行宣告操作请求</p>
<p>错误响应: OnErrRtnExecOrderAction，OnRspExecOrderAction</p>
<p>正确响应: OnRtnExecOrder</p>
<span class="anchor" id="2186f722-17e5-456a-8c85-a8e91a2f0392"></span>
## 1.函数原型
<p>virtual int ReqExecOrderAction(CThostFtdcInputExecOrderActionField *pInputExecOrderAction, int nRequestID) = 0;</p>
<span class="anchor" id="3117bdc6-606e-4d4a-a811-8e4fd74ab844"></span>
## 2.参数
<p>pInputExecOrderAction：输入执行宣告操作</p>
<pre><code>struct CThostFtdcInputExecOrderActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///执行宣告操作引用
    TThostFtdcOrderActionRefType ExecOrderActionRef;
    ///执行宣告引用
    TThostFtdcOrderRefType ExecOrderRef;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///前置编号
    TThostFtdcFrontIDType FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///执行宣告操作编号
    TThostFtdcExecOrderSysIDType ExecOrderSysID;
    ///操作标志
    TThostFtdcActionFlagType ActionFlag;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
};
</code></pre>
<p>ActionFlag：一般都是删除操作，不支持修改</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="7f359e76-0991-43a7-8183-8719b3c68feb"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="718f6be4-dd2d-4499-8f5c-a2467ce8520e"></span>
## 4.调用示例
<pre><code>CThostFtdcInputExecOrderActionField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
a.ExecOrderActionRef = 1;
strcpy_s(a.ExecOrderRef, "00000003");
a.FrontID = 1;
a.SessionID = -7844256;
strcpy_s(a.ExchangeID, "SHFE");
strcpy_s(a.ExecOrderSysID, "         285");
a.ActionFlag = THOST_FTDC_AF_Delete;//删除
strcpy_s(a.UserID, "1000001");
strcpy_s(a.InstrumentID, "rb1809");
m_pUserApi-&gt;ReqExecOrderAction(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="ef789b2f-8192-4dfc-9fcd-e8c7c56aaaeb"></span>
## 5.FAQ
<p>无</p>
