<p>执行宣告操作错误回报，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQEXECORDERACTION/">ReqExecOrderAction</a>后有字段填写不对之类的CTP报错则通过此接口返回</p>
<span class="anchor" id="07b987b1-ed66-4090-9141-971778df6988"></span>
## 1.函数原型
<p>virtual void OnErrRtnExecOrderAction(CThostFtdcExecOrderActionField *pExecOrderAction, CThostFtdcRspInfoField *pRspInfo) {};</p>
<span class="anchor" id="d23ebe62-ae49-4a7d-ba27-9db3d7a75e75"></span>
## 2.参数
<p>pExecOrderAction：执行宣告操作</p>
<pre><code>struct CThostFtdcExecOrderActionField
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
    ///操作日期
    TThostFtdcDateType  ActionDate;
    ///操作时间
    TThostFtdcTimeType  ActionTime;
    ///交易所交易员代码
    TThostFtdcTraderIDType  TraderID;
    ///安装编号
    TThostFtdcInstallIDType InstallID;
    ///本地执行宣告编号
    TThostFtdcOrderLocalIDType  ExecOrderLocalID;
    ///操作本地编号
    TThostFtdcOrderLocalIDType  ActionLocalID;
    ///会员代码
    TThostFtdcParticipantIDType ParticipantID;
    ///客户代码
    TThostFtdcClientIDType  ClientID;
    ///业务单元
    TThostFtdcBusinessUnitType  BusinessUnit;
    ///报单操作状态
    TThostFtdcOrderActionStatusType OrderActionStatus;
    ///用户代码
    TThostFtdcUserIDType    UserID;
    ///执行类型
    TThostFtdcActionTypeType    ActionType;
    ///状态信息
    TThostFtdcErrorMsgType  StatusMsg;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///营业部编号
    TThostFtdcBranchIDType  BranchID;
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
<p>ActionFlag：支持删除操作，不支持修改</p>
<p>InstallID：CTP内部使用</p>
<p>OrderActionStatus：报单的状态</p>
<p>StatusMsg：错误的信息</p>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<span class="anchor" id="ce14fb45-732e-465b-adc1-2a5a96b5a2c7"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="1d868456-5191-4477-9fbb-490c6baf4442"></span>
## 4.FAQ
<p>无</p>
