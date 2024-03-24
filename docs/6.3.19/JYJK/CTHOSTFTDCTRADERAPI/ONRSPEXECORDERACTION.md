<p>执行宣告操作请求响应，当执行ReqExecOrderAction后，该方法被调用</p>
<span class="anchor" id="e0ecb60c-1476-4836-8a3f-1b3b2811fc80"></span>
## 1.函数原型
<p>virtual void OnRspExecOrderAction(CThostFtdcInputExecOrderActionField *pInputExecOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="0cea8fed-6b4a-4e3d-b5d4-8deeebc1a65c"></span>
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
<p>ActionFlag：撤单标志，目前只有删除（撤单功能），没有修改（改单功能）。</p>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="bfa9330d-a3bc-4f08-97b4-b63c830e7a9d"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="12bf7ccb-20e7-42a7-ba9d-07bf1d31c356"></span>
## 4.FAQ
<p>无</p>
