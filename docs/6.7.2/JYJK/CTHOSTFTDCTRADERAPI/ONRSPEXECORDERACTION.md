<p>执行宣告操作请求响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQEXECORDERACTION/">ReqExecOrderAction</a>后，该方法被调用</p>
<span class="anchor" id="dfa186f2-7981-4f28-a164-5a525aae5cd4"></span>
## 1.函数原型
<p>virtual void OnRspExecOrderAction(CThostFtdcInputExecOrderActionField *pInputExecOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="21d78a85-0f5d-401a-9656-98e4148f7243"></span>
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
<span class="anchor" id="6841234b-9cde-4047-af2d-df7b5e5b166d"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="52d2f6fa-5c85-4dd6-9a4e-70fdc7dc8b28"></span>
## 4.FAQ
<p>无</p>
