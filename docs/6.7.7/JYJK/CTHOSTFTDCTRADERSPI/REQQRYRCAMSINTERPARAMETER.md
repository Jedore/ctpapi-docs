<p>请求RCAMS跨品种风险折抵参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRCAMSINTERPARAMETER/">OnRspQryRCAMSInterParameter</a></p>
<span class="anchor" id="cf158604-13fb-4759-9222-7cca11f6f3b9"></span>
## 1.函数原型
<p>virtual int ReqQryRCAMSInterParameter(CThostFtdcQryRCAMSInterParameterField *pQryRCAMSInterParameter, int nRequestID) = 0;</p>
<span class="anchor" id="5abf23ab-c7f4-4fb0-a774-c9dd7fc8c684"></span>
## 2.参数
<p>pQryRCAMSInterParameter：RCAMS跨品种风险折抵参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">ProductGroupID</td>
<td style="TEXT-ALIGN: left;">商品群代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">CombProduct1</td>
<td style="TEXT-ALIGN: left;">产品组合代码1</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">CombProduct2</td>
<td style="TEXT-ALIGN: left;">产品组合代码2</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<span class="anchor" id="b60db4b6-e331-4962-a0f6-95fc1962d8b0"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="0c40291f-0c0f-47bd-af9c-d00c25333ac0"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="1d0b359d-277c-4bf4-bf6e-63a19af40213"></span>
## 5.FAQ
<p>无</p>
