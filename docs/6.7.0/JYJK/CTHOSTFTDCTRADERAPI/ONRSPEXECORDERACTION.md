<p>执行宣告操作请求响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQEXECORDERACTION/">ReqExecOrderAction</a>后，该方法被调用</p>
<span class="anchor" id="86b2c236-1ff8-40d0-8991-0d01d3772437"></span>
## 1.函数原型
<p>virtual void OnRspExecOrderAction(CThostFtdcInputExecOrderActionField *pInputExecOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="d9200e25-1d24-4b02-8706-21b79894227f"></span>
## 2.参数
<p>pInputExecOrderAction：输入执行宣告操作</p>
<pre><code>struct CThostFtdcInputExecOrderActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///执行宣告操作引用
    TThostFtdcOrderActionRefType    ExecOrderActionRef;
    ///执行宣告引用
    TThostFtdcOrderRefType  ExecOrderRef;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///前置编号
    TThostFtdcFrontIDType   FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///执行宣告操作编号
    TThostFtdcExecOrderSysIDType    ExecOrderSysID;
    ///操作标志
    TThostFtdcActionFlagType    ActionFlag;
    ///用户代码
    TThostFtdcUserIDType    UserID;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///保留的无效字段
    TThostFtdcOldIPAddressType  reserve2;
    ///Mac地址
    TThostFtdcMacAddressType    MacAddress;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
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
<span class="anchor" id="a115f031-c364-4447-ae27-23d64d451a18"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="bd2a2c6b-d865-4fbc-b2cb-fabcb2a8b9c9"></span>
## 4.FAQ
<p>无</p>
