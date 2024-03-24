<p>批量报单操作错误回报</p>
<span class="anchor" id="503fef0d-9f9a-4136-8f70-0f65572efe88"></span>
## 1.函数原型
<p>virtual void OnErrRtnBatchOrderAction(CThostFtdcBatchOrderActionField *pBatchOrderAction, CThostFtdcRspInfoField *pRspInfo) {};</p>
<span class="anchor" id="5bb1134b-ae9e-404f-979b-6d505414af2a"></span>
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
<span class="anchor" id="0a7b113e-37f4-4a09-bf55-40d40926945f"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="526b7fb7-0011-4937-8c7a-765aceeca5ef"></span>
## 4.FAQ
<p>无</p>
