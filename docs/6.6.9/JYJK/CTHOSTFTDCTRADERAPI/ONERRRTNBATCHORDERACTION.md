<p>批量报单操作错误回报</p>
<span class="anchor" id="52ebe0e6-7a06-4cde-b3ae-1a594359fb7c"></span>
## 1.函数原型
<p>virtual void OnErrRtnBatchOrderAction(CThostFtdcBatchOrderActionField *pBatchOrderAction, CThostFtdcRspInfoField *pRspInfo) {};</p>
<span class="anchor" id="a1d7cc56-21e5-4aa8-b264-48069379a9fd"></span>
## 2.参数
<p>pBatchOrderAction：批量报单操作</p>
<pre><code>struct CThostFtdcBatchOrderActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///报单操作引用
    TThostFtdcOrderActionRefType    OrderActionRef;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///前置编号
    TThostFtdcFrontIDType   FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///操作日期
    TThostFtdcDateType  ActionDate;
    ///操作时间
    TThostFtdcTimeType  ActionTime;
    ///交易所交易员代码
    TThostFtdcTraderIDType  TraderID;
    ///安装编号
    TThostFtdcInstallIDType InstallID;
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
    ///状态信息
    TThostFtdcErrorMsgType  StatusMsg;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///保留的无效字段
    TThostFtdcOldIPAddressType  reserve1;
    ///Mac地址
    TThostFtdcMacAddressType    MacAddress;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
};
</code></pre>
<p>OrderActionStatus：撤单后报单的状态</p>
<p>StatusMsg：撤单错误的状态信息，如果没有错误的则返回0</p>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<span class="anchor" id="7f3dadd3-e0f9-4797-912c-f5c6bf61b9fd"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="e783d649-a6de-4704-bf8a-96a27e68849f"></span>
## 4.FAQ
<p>无</p>
